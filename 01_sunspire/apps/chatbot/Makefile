CC = gcc
CFLAGS = -Wall -Wextra -O2
# Note: -Wformat=0 disables format string warnings (intentional for CTF)
CFLAGS_VULN = -Wall -Wextra -O2 -Wno-format-security

TARGET = chatbot
SRC = main.c

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS_VULN) -o $(TARGET) $(SRC)

clean:
	rm -f $(TARGET)

install: $(TARGET)
	cp $(TARGET) /opt/chatbot/
	cp chatbot.service /etc/systemd/system/
	systemctl daemon-reload
	systemctl enable chatbot
	systemctl start chatbot

.PHONY: all clean install
