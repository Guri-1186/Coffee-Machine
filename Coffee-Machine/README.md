# Coffee Machine Project

A Python-based digital coffee machine simulator that replicates the functionality of a real coffee machine with additional features like payment processing, admin controls, and website integration.

## Features

- Multiple drink options (Americano, Espresso, Latte, Cappuccino)
- Resource management (water, milk, coffee)
- Payment processing with multiple options:
  - Cash payments with change calculation
  - Card payments
  - Currency: GEL (Georgian Lari)
- Admin controls for machine operations:
  - Resource refilling
  - Machine shutdown
  - Password protection
- Integration with online coffee house website
- Detailed reporting system for resources and profits
- Comprehensive error handling

## System Requirements

- Python 3.x
- Required packages (listed in requirements.txt):
  - `requests==2.31.0` (for website connectivity)
  - `webbrowser` (built-in, for opening the coffee house website)

## Project Structure

### Core Classes

1. **Menu Class**
   - Loads and manages menu data from JSON file
   - Provides drink options and details
   - Handles menu file error cases
2. **Drink Class**

   - Manages individual drink properties
   - Stores ingredients and cost information

3. **CoffeeMachine Class**

   - Manages machine resources (water, milk, coffee)
   - Validates resource availability
   - Handles drink preparation
   - Generates resource reports

4. **MoneyMachine Class**

   - Processes payments (cash/card)
   - Handles change calculation
   - Tracks profits
   - Manages GEL currency transactions

5. **Admin Class**

   - Controls administrative functions
   - Manages password protection
   - Handles resource refilling
   - Controls machine shutdown

6. **Website Integration**
   - Connects to Coffee House website
   - Checks website availability
   - Opens website in browser

## Installation and Setup

1. Clone the repository
2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the JSON data file is present in the correct location:
   `Final_Project_Coffee_Machine/data/coffee_shop_data.json`

## Usage Guide

### Starting the Machine

Run the main program:

```bash
python main.py
```

### Available Commands

- Drink selection: Enter drink name (espresso/latte/cappuccino/americano)
- Administrative:
  - `report`: View resource and profit status
  - `refill`: Refill resources (requires admin password)
  - `off`: Shutdown machine (requires admin password)

### Ordering Process

1. Select desired drink
2. System checks resource availability
3. Choose payment method (cash/card)
4. Complete payment
5. Receive drink
6. Optional: Visit coffee house website

### Admin Functions

- Default password: "CM1186"
- Available operations:
  - Machine shutdown
  - Resource refilling
  - System reports

## Initial Resources

The machine initializes with:

- Water: 300ml
- Milk: 200ml
- Coffee: 100g

## Error Handling

The system handles various error scenarios:

- Insufficient resources
- Invalid payment amounts
- Incorrect admin password
- JSON file errors
- Website connectivity issues
- Invalid user inputs

## Website Integration

- URL: https://coffee-house2.netlify.app/
- Features:
  - Automatic availability checking
  - Browser opening functionality
  - Error handling for connection issues
