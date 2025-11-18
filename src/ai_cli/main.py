import os
import time
import sys
from groq import Groq
import shutil # Added for terminal size detection
import textwrap # Added for intelligent word wrapping

# --- Configuration Constant ---
GROQ_MODEL = "llama-3.1-8b-instant"
# ------------------------------

def loadingbar(valueseconds):
    """Displays a simple progress bar."""
    
    def progress_bar(iteration, total, prefix='', suffix='', decimals=1, bar_length=50):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filled_length = int(bar_length * iteration // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        # Use sys.stdout.write for dynamic update on the same line
        sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
        sys.stdout.flush()

    total_items = 100
    for i in range(total_items + 1):
        time.sleep(valueseconds) # Simulate work
        progress_bar(i, total_items, prefix='Progress:', suffix='Complete', bar_length=40)
    print() # New line after completion

def setup_groq_client():
    """Setup Groq client with API key"""
    # NOTE: The provided key is a placeholder. Replace with your actual Groq API key 
    # for production use. For this exercise, we keep the user's hardcoded value.
    api_key = "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"
    
    try:
        # Initialize the Groq client
        client = Groq(api_key=api_key)
        return client
    except Exception as e:
        print(f"Error setting up Groq client: {e}")
        return None

def send_groq_message(client, messages, model):
    """
    Sends the complete message history to Groq for a context-aware response.
    
    Args:
        client (Groq): Initialized Groq client.
        messages (list[dict]): List of message objects in the format 
                               [{"role": "user", "content": "..."}]
        model (str): The Groq model to use.
        
    Returns:
        str: The generated response text, or an error message.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=messages, # Pass the entire conversation history
            model=model,
            temperature=0.7,
            max_tokens=1024,
        )
        # Extract the content from the response
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error during Groq API call: {e}"

def llama_chat_session(client, selected_model):
    """
    Start an interactive, multi-turn chat session with the selected Llama model.
    Maintains conversation history using the required list of message objects.
    """
    print("\n🦙 Llama Chat Session Started!")
    print(f"Model: {selected_model}")
    print("Type 'exitmodel' to return to main menu")
    print("Type 'clear' to clear conversation history")
    print("-" * 50)
    
    # conversation_history stores a list of dicts for the API
    conversation_history = []
    
    # --- Terminal Width Detection for Word Wrapping ---
    try:
        # Get terminal columns, falling back to 80 if detection fails
        term_width = shutil.get_terminal_size(fallback=(80, 24)).columns
        # Set the wrap width, leaving 5 characters for padding on the right
        wrap_width = max(40, term_width - 5) 
    except:
        wrap_width = 75 # Safe fallback if terminal size cannot be determined
    # ---------------------------------------------------
        
    while True:
        user_message = input("\nYou: ").strip()
        
        if user_message.lower() == 'exitmodel':
            print("Exiting Llama chat session...")
            break
        elif user_message.lower() == 'clear':
            conversation_history = []
            print("Conversation history cleared!")
            continue
        elif not user_message:
            continue
        
        print("🤔 Llama is thinking...", end="")
        
        # 1. Add the new user message to the history
        conversation_history.append({"role": "user", "content": user_message})
        
        # 2. Limit the history sent to the API to save tokens (e.g., last 10 messages)
        # This is passed directly to the 'messages' argument of the API call.
        messages_to_send = conversation_history[-10:] 
        
        # 3. Get the response
        response = send_groq_message(client, messages_to_send, selected_model)
        
        # 4. Wrap the response text before printing
        prefix = "🦙 Llama: "
        wrapped_response = textwrap.fill(
            response, 
            width=wrap_width, 
            initial_indent=prefix,
            subsequent_indent=" " * len(prefix)
        )
        
        # 5. Remove the thinking message and print the full response
        # Using carriage return to clear the 'thinking' message
        sys.stdout.write("\r" + " " * 30 + "\r")
        sys.stdout.flush()
        
        # Print the properly wrapped response (which already includes the prefix)
        print(wrapped_response)
        
        # 6. Store the assistant's response back into the full history (for future context)
        if not response.startswith("Error:"):
            # Store the *original* response for context, not the wrapped one
            conversation_history.append({"role": "assistant", "content": response})

def cli():
    """The main entry point for the CLI."""
    # ASCII Art Display
    print(r"""   _____  .___ 
  /  _  \ |   |
 /  /_\  \|   |
/    |    \   |
\____|__  /___|
        \/        
               """)

    print(r"""_________ .____    .___ 
\_   ___ \|    |   |   |
/    \  \/|    |   |   |
\     \___|    |___|   |
 \______  /_______ \___|
        \/        \/    """)

    print("Welcome to AI CLI!")
    print("Enter help to see available commands.")

    # Local variables for the session
    groq_client = None
    selected_model = None

    loop = 0
    while loop == 0:
        userinput = str(input("\nUser: ")).strip().lower() # Make input handling case-insensitive
        
        if userinput == "help":
            print("Available commands:")
            print("help - Show this help message")
            print("exit - Exit the AI CLI")
            print("model - Select AI model (Starts chat immediately upon successful selection)")
            print("chat - Start a chat session (only needed if model is already selected and you exited the chat)")
            print("version - Display version information")
            print("test - Test Groq connection")
        
        elif userinput == "version":
            print("AI CLI Version 1.5.0 - Now with proper word wrapping for terminal output!")
        
        elif userinput == "exit":
            print("Exiting AI CLI. Goodbye!")
            loop = 1
        
        elif userinput == "test":
            print("Testing Groq connection...")
            test_client = setup_groq_client()
            if test_client:
                # Test using the single specified Groq model
                test_messages = [{"role": "user", "content": "Say hello and introduce yourself as Llama 3.1 8B Instant! Write a short sentence that is long enough to test word wrapping."}]
                response = send_groq_message(test_client, test_messages, GROQ_MODEL)
                print(f"✅ Connection successful!\n🦙 Response: {response}")
            else:
                print("❌ Connection failed! Check your API key and network connection.")
        
        elif userinput == "model":
            print("To go back, enter 'back'")
            print("Available models:")
            print(f"1. Llama 3.1 8B Instant (via Groq)")
            print("2. Gemini Flash (Not implemented)")
            
            model_choice = str(input("Select a model (1 or 2): ")).strip()
            
            if model_choice == "1":
                loadingbar(0.05)
                print(f"🦙 {GROQ_MODEL} selected.")
                groq_client = setup_groq_client()
                if groq_client:
                    print("✅ Model loaded successfully. Starting chat session...")
                    selected_model = GROQ_MODEL
                    # Start chat immediately after successful selection
                    llama_chat_session(groq_client, selected_model)
                else:
                    print("❌ Failed to load model. Check setup.")
                    selected_model = None
            elif model_choice == "2":
                loadingbar(0.05)
                print("Gemini Flash selected.")
                print("⚠️  Gemini Flash integration not yet implemented.")
                selected_model = "gemini"
            elif model_choice.lower() == "back":
                continue
            else:
                print("Invalid model selection.")
        
        elif userinput == "chat":
            if not groq_client or not selected_model:
                print("❌ Please select a Llama model first using the 'model' command.")
            elif selected_model == GROQ_MODEL:
                llama_chat_session(groq_client, selected_model)
            else:
                print("❌ Chat not available for selected model.")
                
        else:
            print("Invalid command. Type 'help' to see available commands.")