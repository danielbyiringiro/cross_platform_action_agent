import re
import random
import logging
import time
from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('email_agent.log'),
        logging.StreamHandler()
    ]
)

class EmailProvider(ABC):
    """Abstract base class for email providers"""
    
    def __init__(self, page):
        self.page = page
        self.llm = MockLLM()
    
    @abstractmethod
    def login(self, username: Optional[str] = None, password: Optional[str] = None):
        pass
    
    @abstractmethod
    def execute_send_email(self, to: str, subject: str, body: str):
        pass
    
    def human_delay(self):
        """Simulate human delay"""
        time.sleep(random.uniform(0.5, 2.5))
    
    def human_mouse_movement(self, element):
        """Simulate human-like mouse movement"""
        self.human_delay()

class MockLLM:
    """Mock LLM for instruction interpretation"""
    
    def interpret_instruction(self, instruction: str) -> Dict:
        logging.info(f"Interpreting instruction: {instruction}")
        
        # Enhanced pattern matching with fallbacks
        patterns = {
            'to': [
                r'(?:to|for|recipient).*?([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})',
                r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
            ],
            'subject': [
                r'(?:subject|about|re).*?"([^"]+)"',
                r'(?:subject|about|re)\s+([^"]+?)(?=\s+(?:body|saying|content|$))'
            ],
            'body': [
                r'(?:body|content|saying).*?"([^"]+)"',
                r'(?:body|content|saying)\s+([^"]+?)$'
            ]
        }
        
        extracted = {}
        for key, pattern_list in patterns.items():
            for pattern in pattern_list:
                match = re.search(pattern, instruction, re.IGNORECASE)
                if match:
                    extracted[key] = match.group(1).strip()
                    break
            if key not in extracted:
                extracted[key] = ""  # Default empty
        
        return extracted

class GmailProvider(EmailProvider):
    def __init__(self, page):
        super().__init__(page)
        self.selectors = {
            'compose': ["div[gh='cm']"],
            'to': ["input[aria-label*='To']"],
            'subject': ["input[name='subjectbox']"],
            'body': ["div[aria-label*='Message Body']"],
            'send': ["div[aria-label*='Send']"]
        }
    
    def safe_click(self, selector_type, retries=3):
        """Mock clicking an element"""
        logging.info(f"MOCK: Clicking {selector_type} element")
        self.human_delay()
        return True
    
    def safe_fill(self, selector_type, value, retries=2):
        """Mock filling a field"""
        logging.info(f"MOCK: Filling {selector_type} with '{value}'")
        self.human_delay()
        return True
    
    def login(self, username: Optional[str] = None, password: Optional[str] = None):
        """Mock Gmail login process"""
        logging.info("MOCK: Navigating to Gmail")
        self.human_delay()
        logging.info("MOCK: Gmail inbox loaded successfully")
        return True
    
    def _handle_email_suggestions(self, expected_email: str):
        """Mock handling Gmail's email autocomplete suggestions"""
        logging.info("MOCK: Handling email suggestions")
        self.human_delay()
        logging.info("MOCK: Pressed Enter to accept suggestion")
        return True
    
    def execute_send_email(self, to: str, subject: str, body: str):
        """Mock Gmail email sending process"""
        logging.info(f"MOCK: Preparing to send email to {to} via Gmail")
        self.human_delay()
        
        # Simulate compose
        logging.info("MOCK: Clicking compose button")
        self.human_delay()
        
        # Simulate recipient entry with autocomplete
        logging.info(f"MOCK: Entering recipient: {to}")
        self._handle_email_suggestions(to)
        
        # Simulate subject entry
        logging.info(f"MOCK: Entering subject: {subject}")
        self.human_delay()
        
        # Simulate body entry
        logging.info(f"MOCK: Entering body: {body}")
        self.human_delay()
        
        # Simulate sending
        logging.info("MOCK: Sending email with Ctrl+Enter shortcut")
        self.human_delay()
        logging.info("MOCK: Gmail email sent successfully")
        
        return True

class OutlookProvider(EmailProvider):
    def __init__(self, page):
        super().__init__(page)
        # MOCKED: Microsoft's bot detection prevents reliable selector usage
        self.selectors = {
            'compose': ["button[aria-label*='New message']"],
            'to': ["input[placeholder*='Add recipients']"],
            'subject': ["input[placeholder*='Add a subject']"],
            'body': ["div[aria-label*='Message body']"],
            'send': ["button[aria-label*='Send']"]
        }
    
    def safe_click(self, selector_type, retries=3):
        """MOCKED: Microsoft's bot detection prevents reliable element interaction"""
        logging.info(f"MOCK: Attempting to click {selector_type} in Outlook")
        self.human_delay()
        
        # Simulate bot detection 30% of the time
        if random.random() < 0.3:
            logging.error("MOCK: Microsoft bot detection blocked interaction")
            return False
            
        logging.info(f"MOCK: Successfully clicked {selector_type}")
        return True
    
    def safe_fill(self, selector_type, value, retries=2):
        """MOCKED: Microsoft's bot detection prevents reliable form filling"""
        logging.info(f"MOCK: Attempting to fill {selector_type} in Outlook")
        self.human_delay()
        
        # Simulate bot detection 40% of the time
        if random.random() < 0.4:
            logging.error("MOCK: Microsoft bot detection blocked form filling")
            return False
            
        logging.info(f"MOCK: Successfully filled {selector_type} with '{value}'")
        return True
    
    def login(self, username: Optional[str] = None, password: Optional[str] = None):
        """
        MOCKED: Microsoft's advanced bot detection prevents reliable Outlook automation.
        In a real implementation, this would handle the complex authentication flow.
        """
        logging.info("MOCK: Navigating to Outlook")
        self.human_delay()
        
        # Simulate Microsoft's authentication challenges
        auth_steps = [
            "Loading Office 365 login page",
            "Checking existing sessions",
            "Detecting automation patterns",
            "Presenting password challenge",
            "Verifying credentials",
            "Checking multi-factor authentication requirements"
        ]
        
        for step in auth_steps:
            logging.info(f"MOCK: {step}")
            self.human_delay()
            
            # Simulate authentication failure due to bot detection
            if "automation patterns" in step and random.random() < 0.6:
                logging.error("MOCK: Microsoft bot detection blocked authentication")
                raise Exception("Authentication failed: Bot detection triggered")
        
        logging.info("MOCK: Outlook inbox loaded successfully")
        return True
    
    def execute_send_email(self, to: str, subject: str, body: str):
        """
        MOCKED: Microsoft's robust bot detection prevents reliable Outlook automation.
        This demonstrates the ideal flow that would work if not for detection mechanisms.
        """
        logging.info(f"MOCK: Preparing to send email to {to} via Outlook")
        self.human_delay()
        
        # Simulate the email composition process
        steps = [
            "Locating compose button",
            "Opening new message window",
            "Focusing recipient field",
            "Handling Outlook's recipient validation",
            "Focusing subject field",
            "Focusing body editor",
            "Executing send command"
        ]
        
        for step in steps:
            logging.info(f"MOCK: {step}")
            self.human_delay()
            
            # Simulate Outlook's unique UI challenges
            if "recipient" in step:
                logging.info("MOCK: Handling Outlook's recipient suggestions")
                self.human_delay()
                
            # Simulate bot detection interference
            if random.random() < 0.25:
                logging.warning("MOCK: Microsoft bot detection causing minor delays")
                self.human_delay()
        
        # Final send attempt
        logging.info("MOCK: Attempting to send email")
        self.human_delay()
        
        # Simulate success or failure based on bot detection
        if random.random() < 0.7:
            logging.info("MOCK: Outlook email sent successfully")
            return True
        else:
            logging.error("MOCK: Microsoft bot detection blocked email sending")
            raise Exception("Send failed: Bot detection triggered")

class MockBrowser:
    """Mock browser for simulating Playwright functionality"""
    
    def new_page(self):
        """Return a mock page object"""
        return MockPage()
    
    def close(self):
        """Mock browser close"""
        logging.info("MOCK: Closing browser")

class MockPage:
    """Mock page object for simulating Playwright page interactions"""
    
    def goto(self, url, wait_until="networkidle", timeout=30000):
        """Mock page navigation"""
        logging.info(f"MOCK: Navigating to {url}")
        time.sleep(1)
        return True
    
    def wait_for_selector(self, selector, timeout=5000):
        """Mock waiting for selector"""
        logging.info(f"MOCK: Waiting for selector {selector}")
        time.sleep(0.5)
        return MockElement()
    
    def click(self, selector, timeout=5000):
        """Mock clicking an element"""
        logging.info(f"MOCK: Clicking {selector}")
        time.sleep(0.5)
        return True
    
    def evaluate(self, script):
        """Mock page evaluation"""
        if "navigator.platform" in script:
            return "Win32"  # Simulate Windows platform
        return None
    
    def keyboard(self):
        """Mock keyboard interface"""
        return MockKeyboard()
    
    def screenshot(self, path):
        """Mock screenshot capability"""
        logging.info(f"MOCK: Taking screenshot saved to {path}")
        return True
    
    def close(self):
        """Mock page close"""
        logging.info("MOCK: Closing page")

class MockElement:
    """Mock element for simulating DOM interactions"""
    
    def click(self):
        """Mock element click"""
        logging.info("MOCK: Clicking element")
        time.sleep(0.2)
        return True
    
    def fill(self, value):
        """Mock element fill"""
        logging.info(f"MOCK: Filling element with '{value}'")
        time.sleep(0.3)
        return True
    
    def press(self, key):
        """Mock key press"""
        logging.info(f"MOCK: Pressing key {key}")
        time.sleep(0.1)
        return True
    
    def bounding_box(self):
        """Mock bounding box"""
        return {'x': 100, 'y': 100, 'width': 200, 'height': 50}

class MockKeyboard:
    """Mock keyboard for simulating keyboard interactions"""
    
    def press(self, key_combination):
        """Mock key press"""
        logging.info(f"MOCK: Pressing keys {key_combination}")
        time.sleep(0.2)
        return True
    
    def type(self, text, delay=None):
        """Mock typing"""
        logging.info(f"MOCK: Typing '{text}'")
        time.sleep(0.5)
        return True

class EmailAgent:
    def __init__(self, headless: bool = False, user_data_dir: Optional[str] = None):
        """Mock email agent initialization"""
        logging.info("MOCK: Initializing email agent")
        self.browser = MockBrowser()
        self.llm = MockLLM()
    
    def execute_task(self, instruction: str, providers: List[str]):
        """Mock task execution across multiple email providers"""
        results = {}
        
        for provider_name in providers:
            logging.info(f"Processing with {provider_name}")
            
            # Create a new mock page
            page = self.browser.new_page()
            
            if provider_name == 'gmail':
                provider = GmailProvider(page)
            elif provider_name == 'outlook':
                provider = OutlookProvider(page)
            else:
                raise ValueError(f"Unsupported provider: {provider_name}")
            
            try:
                # Extract email components
                email_data = self.llm.interpret_instruction(instruction)
                
                # Navigate and login
                provider.login()
                
                # Execute the send email process
                provider.execute_send_email(
                    email_data['to'], 
                    email_data['subject'], 
                    email_data['body']
                )
                
                results[provider_name] = "Success"
                logging.info(f"Email sent successfully via {provider_name}")
                
            except Exception as e:
                results[provider_name] = f"Failed: {str(e)}"
                logging.error(f"Failed to send email via {provider_name}: {str(e)}")
                
            finally:
                time.sleep(1)  # Wait to observe result
                page.close()
        
        return results
    
    def close(self):
        """Mock agent cleanup"""
        logging.info("MOCK: Closing email agent")
        self.browser.close()

# CLI Interface
if __name__ == "__main__":
    import sys
    import json
    
    if len(sys.argv) < 2:
        print("Usage: python email_agent.py \"Send email to recipient@example.com about 'Test Subject' saying 'Hello World'\"")
        sys.exit(1)
    
    instruction = sys.argv[1]
    
    # Initialize agent
    agent = EmailAgent(headless=False, user_data_dir="./userdata")
    
    try:
        results = agent.execute_task(instruction, ['gmail', 'outlook'])
        print("Execution Results:")
        for provider, result in results.items():
            print(f"{provider}: {result}")
    except Exception as e:
        logging.error(f"Critical error: {str(e)}")
    finally:
        agent.close()