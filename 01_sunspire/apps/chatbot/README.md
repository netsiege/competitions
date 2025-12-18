# Sunspire Energy Support Chatbot

A TCP-based chatbot for Sunspire energy support inquiries, written in C.

## Building

```bash
make
```

Or manually:
```bash
gcc -Wall -Wno-format-security -o chatbot main.c
```

## Running

```bash
./chatbot
# Listens on port 5985
```

## Connecting

```bash
nc <host> 5985
```

## Available Commands

- `hello` - Greeting
- `help` - List available topics
- `status` - System status
- `hours` - Support hours
- `location` - HQ location
- `contact` - Contact information
- `pricing` - Energy rates
- `outage` - Outage status
- `solar` - Solar generation stats
- `wind` - Wind generation stats
- `billing` - Billing inquiries (requires auth)
- `weather` - Weather forecast
- `auth` - Begin authentication
- `bye` / `quit` / `exit` - Disconnect

## Deployment

```bash
make install
```

Or manually:
```bash
mkdir -p /opt/chatbot
cp chatbot /opt/chatbot/
cp chatbot.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable chatbot
systemctl start chatbot
```
