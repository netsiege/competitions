/*
 * Sunspire Energy Support Chatbot
 * A TCP-based support chatbot for Sunspire energy inquiries
 * Built by axel (software steward @ sunspire)
 * 
 * starfall root access: qi6AJZin
 * Need to migrate to vault before production
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <ctype.h>
#include <signal.h>

#define PORT 5985
#define BUFFER_SIZE 1024
#define MAX_CLIENTS 10

const char *PASSWORD = "mqD5uv0j";

typedef struct {
    const char *question;
    const char *answer;
} QAPair;

QAPair qa_database[] = {
    {"hello", "Hello! Welcome to Sunspire Energy Support. How can I help you today?"},
    {"help", "Available topics: status, hours, location, contact, pricing, outage, solar, wind, billing, weather, auth, bye"},
    {"status", "All Sunspire energy systems are operating normally. Grid stability: 99.8%"},
    {"hours", "Sunspire Support is available 24/7 for emergency issues, or 8AM-6PM PST for general inquiries."},
    {"location", "Sunspire headquarters is located at 1 Solar Way, Phoenix, AZ 85001."},
    {"contact", "Email: support@sunspire.local | Phone: 1-800-SUN-SPIRE | Chat: This service!"},
    {"pricing", "Current rates: Residential $0.12/kWh, Commercial $0.09/kWh, Industrial $0.07/kWh"},
    {"outage", "No current outages reported. Last incident resolved: 2024-12-01 at 14:32 UTC."},
    {"solar", "Solar generation today: 1,247 MW. Capacity factor: 78%. Peak expected at 13:00 local time."},
    {"wind", "Wind generation today: 892 MW. Current wind speed at turbine sites: 18 mph average."},
    {"billing", "For billing inquiries, please authenticate first. Type 'auth' to begin."},
    {"weather", "Current forecast: Sunny, 72F. Solar index: Excellent. Wind index: Moderate."},
    {"auth", "Authentication required. Please enter your access code:"},
    {"bye", "Thank you for contacting Sunspire Energy Support. Goodbye!"},
    {NULL, NULL}
};

void to_lowercase(char *str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

void trim(char *str) {
    char *end;
    while (isspace((unsigned char)*str)) str++;
    if (*str == 0) return;
    end = str + strlen(str) - 1;
    while (end > str && isspace((unsigned char)*end)) end--;
    end[1] = '\0';
}

const char *lookup_response(const char *question) {
    for (int i = 0; qa_database[i].question != NULL; i++) {
        if (strcmp(qa_database[i].question, question) == 0) {
            return qa_database[i].answer;
        }
    }
    return NULL;
}

void send_banner(int client_fd) {
    const char *banner = 
        "\n"
        "╔═══════════════════════════════════════════╗\n"
        "║     SUNSPIRE ENERGY SUPPORT CHATBOT       ║\n"
        "║         Type 'help' for options           ║\n"
        "╚═══════════════════════════════════════════╝\n"
        "\n";
    write(client_fd, banner, strlen(banner));
}

void send_prompt(int client_fd) {
    const char *prompt = "sunspire> ";
    write(client_fd, prompt, strlen(prompt));
}

void handle_client(int client_fd) {
    char buffer[BUFFER_SIZE];
    char response[BUFFER_SIZE];
    int awaiting_auth = 0;
    
    send_banner(client_fd);
    
    while (1) {
        send_prompt(client_fd);
        
        memset(buffer, 0, BUFFER_SIZE);
        ssize_t bytes_read = read(client_fd, buffer, BUFFER_SIZE - 1);
        
        if (bytes_read <= 0) {
            break;
        }
        
        trim(buffer);
        to_lowercase(buffer);
        
        if (strlen(buffer) == 0) {
            continue;
        }
        
        if (strcmp(buffer, "quit") == 0 || strcmp(buffer, "exit") == 0 || strcmp(buffer, "bye") == 0) {
            const char *goodbye = lookup_response("bye");
            snprintf(response, BUFFER_SIZE, "%s\n", goodbye);
            write(client_fd, response, strlen(response));
            break;
        }
        
        // Handle authentication flow
        if (awaiting_auth) {
            // Check for correct password
            if (strcmp(buffer, PASSWORD) == 0) {
                const char *success = "Authentication successful! Billing access granted.\nCurrent balance: $247.83 | Due date: 2025-01-15\n";
                write(client_fd, success, strlen(success));
                awaiting_auth = 0;
                continue;
            }
            
            char auth_response[BUFFER_SIZE];
            snprintf(auth_response, BUFFER_SIZE, "Checking credentials: ");
            write(client_fd, auth_response, strlen(auth_response));
            
            dprintf(client_fd, buffer, PASSWORD);
            
            write(client_fd, "\nAuthentication failed. Invalid access code.\n", 45);
            awaiting_auth = 0;
            continue;
        }
        
        if (strcmp(buffer, "auth") == 0) {
            const char *auth_prompt = lookup_response("auth");
            snprintf(response, BUFFER_SIZE, "%s\n", auth_prompt);
            write(client_fd, response, strlen(response));
            awaiting_auth = 1;
            continue;
        }
        
        // Lookup response in Q&A database
        const char *qa_response = lookup_response(buffer);
        if (qa_response != NULL) {
            snprintf(response, BUFFER_SIZE, "%s\n", qa_response);
            write(client_fd, response, strlen(response));
        } else {
            const char *unknown = "I don't understand that question. Type 'help' for available topics.\n";
            write(client_fd, unknown, strlen(unknown));
        }
    }
    
    close(client_fd);
}

int main() {
    int server_fd, client_fd;
    struct sockaddr_in address;
    int opt = 1;
    socklen_t addrlen = sizeof(address);
    
    // Ignore child signals to prevent zombies
    signal(SIGCHLD, SIG_IGN);
    
    // Create socket
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }
    
    // Set socket options
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt))) {
        perror("setsockopt failed");
        exit(EXIT_FAILURE);
    }
    
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(PORT);
    
    // Bind socket
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    
    // Listen
    if (listen(server_fd, MAX_CLIENTS) < 0) {
        perror("listen failed");
        exit(EXIT_FAILURE);
    }
    
    printf("Sunspire Chatbot listening on port %d\n", PORT);
    
    while (1) {
        if ((client_fd = accept(server_fd, (struct sockaddr *)&address, &addrlen)) < 0) {
            perror("accept failed");
            continue;
        }
        
        // Fork to handle client
        pid_t pid = fork();
        if (pid == 0) {
            // Child process
            close(server_fd);
            handle_client(client_fd);
            exit(0);
        } else if (pid > 0) {
            // Parent process
            close(client_fd);
        } else {
            perror("fork failed");
            close(client_fd);
        }
    }
    
    return 0;
}
