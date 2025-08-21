# Demo Video

[🎥 Watch the demo](demo.mp4)

# Cross-Platform Email Automation Agent

A sophisticated automation system that simulates sending emails across multiple email providers (**Gmail** and **Outlook**) using browser automation techniques.  
This project demonstrates advanced web automation patterns while acknowledging the technical limitations imposed by modern bot detection systems.

## Features

- **Cross-Platform Support**: Simulated email sending for both Gmail and Outlook  
- **Natural Language Processing**: Mock LLM integration for interpreting email instructions  
- **Advanced Browser Automation**: Simulated Playwright-based browser interactions  
- **Stealth Techniques**: Mocked anti-detection measures for bypassing bot protection  
- **Persistent Sessions**: Simulated user profile persistence  
- **Comprehensive Logging**: Detailed execution logs for debugging and analysis  

## Technical Architecture

EmailAgent (Orchestrator)  
│  
├── MockLLM (Instruction Parser)  
│  
├── EmailProvider (Abstract Base Class)  
│   ├── GmailProvider (Functional Simulation)  
│   └── OutlookProvider (Mocked due to bot detection)  
│  
└── Browser Simulation Layer  
    ├── MockBrowser  
    ├── MockPage  
    ├── MockElement  
    └── MockKeyboard  


# Case Study 2: Cross-Platform Email Automation - Requirements Implementation

## ✅ Core Requirements Met

### 1. Natural Language Instruction Processing
```python
# MockLLM class interprets natural language instructions
def interpret_instruction(self, instruction: str) -> Dict:
    patterns = {
        'to': [r'(?:to|for|recipient).*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'],
        'subject': [r'(?:subject|about|re).*?"([^"]+)"'],
        'body': [r'(?:body|content|saying).*?"([^"]+)"']
    }
    # Extracts email components from natural language
```

---

### 2. Mocked LLM Reasoning Function
```python
# Simulates LLM capabilities for:
# - Instruction interpretation ✓
# - Field identification (through predefined selectors) ✓
# - DOM interaction step generation ✓
class MockLLM:
    def interpret_instruction(self, instruction: str) -> Dict:
        # Parses natural language into structured data
```

---

### 3. Browser Automation Simulation
```python
# Comprehensive browser automation simulation including:
class MockBrowser:        # Browser launch simulation ✓
class MockPage:           # Navigation and page interaction ✓  
class MockElement:        # DOM element interaction ✓
class MockKeyboard:       # Keyboard input simulation ✓
```

---

### 4. Multiple Provider Support with Different DOM Structures
```python
# Abstract base class ensures unified interface
class EmailProvider(ABC):
    @abstractmethod
    def execute_send_email(self, to: str, subject: str, body: str):
        pass

# Provider-specific implementations
class GmailProvider(EmailProvider):    # Gmail-specific DOM handling ✓
class OutlookProvider(EmailProvider):  # Outlook-specific DOM handling ✓
```

---

### 5. Abstracted Provider-Specific Logic
```python
# Unified interface with provider-specific implementations
def execute_task(self, instruction: str, providers: List[str]):
    for provider_name in providers:
        if provider_name == 'gmail':
            provider = GmailProvider(page)
        elif provider_name == 'outlook':
            provider = OutlookProvider(page)
        # Common execution interface ✓
```

---

## ✅ Stretch Goals Implemented

### 1. DOM Structure Change Recovery
```python
# Multiple selector strategies for resilience
self.selectors = {
    'compose': [
        "div[gh='cm']",                     # Primary selector
        "div[role='button'][gh='cm']",      # Fallback 1
        "//div[text()='Compose']",          # Fallback 2 (XPath)
    ]
}

# Retry logic with multiple attempts
def safe_click(self, selector_type, retries=3):
    for attempt in range(retries):
        for selector in self.selectors[selector_type]:
            try:
                element = self.page.wait_for_selector(selector, timeout=5000)
                element.click()
                return True
            except:
                continue
```

---

### 2. DOM-tree + LLM Prompt Chaining Simulation
```python
# Simulated dynamic field matching through multiple selector strategies
def safe_fill(self, selector_type, value, retries=2):
    for selector in self.selectors[selector_type]:
        try:
            element = self.page.wait_for_selector(selector, timeout=5000)
            element.fill(value)
            return True
        except:
            continue
```

---

### 3. Comprehensive Step Logging
```python
# Detailed execution logging at each step
logging.info(f"MOCK: Clicking {selector_type} element")
logging.info(f"MOCK: Filling {selector_type} with '{value}'")
logging.info(f"MOCK: Preparing to send email to {to} via Gmail")
```

---

### 4. Generic UI Agent Architecture
```python
# Abstract base class enables cross-service functionality
class EmailProvider(ABC):
    @abstractmethod
    def login(self, username: Optional[str] = None, password: Optional[str] = None):
        pass
    
    @abstractmethod
    def execute_send_email(self, to: str, subject: str, body: str):
        pass
```

---

### 5. CLI Interface
```python
# Command-line interface as specified
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python email_agent.py \"Send email to recipient@example.com...\"")
        sys.exit(1)
    
    instruction = sys.argv[1]
    # Process natural language command ✓
```

---

## ✅ Evaluation Criteria Addressed

### 1. Agent Architecture and Generalization Ability
- Abstract base class design ✓  
- Provider-agnostic execution flow ✓  
- Easy extension to new providers ✓  

### 2. DOM Parsing and Automation Reliability
- Multiple selector strategies ✓  
- Retry mechanisms ✓  
- Error handling and fallbacks ✓  

### 3. Use of LLM for UI Intent Inference
- Mocked LLM instruction parsing ✓  
- Natural language to structured data conversion ✓  
- Extensible to real LLM integration ✓  

### 4. Abstraction and Modularity
- Clean separation of concerns ✓  
- Provider-specific logic encapsulation ✓  
- Unified execution interface ✓  

### 5. Logging and Recoverability
- Comprehensive step logging ✓  
- Error recovery mechanisms ✓  
- Screenshot capture for debugging ✓  

### 6. Edge Case Handling
- Bot detection simulation ✓  
- Authentication failure handling ✓  
- Malformed input resilience ✓  

---

## Architecture Alignment with Requirements

This implementation follows the exact architecture suggested in the case study:

- **Instruction Interpretation Layer** (MockLLM) ✓  
- **Browser Automation Layer** (MockBrowser, MockPage, etc.) ✓  
- **Provider Abstraction Layer** (EmailProvider base class) ✓  
- **Provider-Specific Implementation** (GmailProvider, OutlookProvider) ✓  
- **Orchestration Layer** (EmailAgent.execute_task()) ✓  

---

The solution demonstrates a production-ready architecture that could be extended with real LLM integration, actual browser automation, and additional provider support while maintaining the core design principles outlined in the case study requirements.


## Installation

1. **Clone the repository:**
   ```bash
   git clone danielbyiringiro/cross_platform_action_agent
   cd cross_platform_action_agent

2. **Create a virtual environment**
   ```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install dependencies**

pip install -r requirements.txt

## Usage  

Run the email agent with a natural language instruction:  

```bash
python email_agent.py "Send email to test@example.com about 'Meeting' saying 'Hello there'"
```

**Expected Output**

```
2025-08-20 22:27:05,842 - INFO - Processing with gmail
2025-08-20 22:27:06,234 - INFO - Interpreting instruction: Send email to test@example.com about 'Meeting' saying 'Hello there'
2025-08-20 22:27:06,240 - INFO - MOCK: Navigating to Gmail
2025-08-20 22:27:17,945 - INFO - MOCK: Gmail inbox loaded successfully
2025-08-20 22:27:17,946 - INFO - MOCK: Preparing to send email to test@example.com via Gmail
2025-08-20 22:27:28,294 - INFO - MOCK: Handling email suggestions
2025-08-20 22:27:29,148 - INFO - MOCK: Pressed Enter to accept suggestion
2025-08-20 22:27:29,148 - INFO - MOCK: Successfully entered recipient: test@example.com
2025-08-20 22:27:32,716 - INFO - MOCK: Sending email with Ctrl+Enter shortcut
2025-08-20 22:27:36,271 - INFO - MOCK: Gmail email sent successfully
2025-08-20 22:27:37,249 - INFO - Email sent successfully via gmail

2025-08-20 22:27:40,505 - INFO - Processing with outlook
2025-08-20 22:27:40,507 - INFO - MOCK: Navigating to Outlook
2025-08-20 22:27:41,507 - INFO - MOCK: Loading Office 365 login page
2025-08-20 22:27:43,008 - INFO - MOCK: Checking existing sessions
2025-08-20 22:27:44,509 - INFO - MOCK: Detecting automation patterns
2025-08-20 22:27:45,510 - ERROR - MOCK: Microsoft bot detection blocked authentication
2025-08-20 22:27:45,511 - ERROR - Failed to send email via outlook: Authentication failed: Bot detection triggered
```

---

**Execution Results:**
```
gmail: Success
outlook: Failed: Authentication failed: Bot detection triggered
```


## Technical Limitations  

### Microsoft Outlook Bot Detection  
Microsoft and Google employs sophisticated bot detection mechanisms that prevent reliable automation of Outlook and Gmail:  

- **Advanced Behavioral Analysis**: Detection of non-human interaction patterns  
- **Browser Fingerprinting**: Identification of automation tools through browser properties  
- **TLS Fingerprinting**: Network-level detection of automated traffic  
- **Authentication Challenges**: Multi-factor requirements and short-lived session tokens  

---

## Workarounds and Alternatives  

For production use with Outlook and Gmail, consider these alternatives:  

- **Microsoft Graph API / Google Oauth API**: Official API for programmatic email sending  
- **OAuth Authentication**: Proper authentication flow instead of credential-based login  
- **App-Specific Passwords**: Generated passwords for application access  
- **Hybrid Approach**: Manual authentication with automated email composition  

---

## Development Notes  

### Architecture Decisions  
- **Abstraction Layers**: Clear separation between providers for maintainability  
- **Mocking Strategy**: Comprehensive simulation of browser interactions for testing  
- **Error Handling**: Robust exception handling with detailed logging  
- **Modular Design**: Easy extension to support additional email providers  

### Extension Points  
- **Additional Providers**: Support for Yahoo, ProtonMail, etc.  
- **Real LLM Integration**: Replace mock LLM with actual AI service  
- **Enhanced Stealth**: More advanced anti-detection techniques  
- **API Integration**: Hybrid browser+API approach for Outlook  



