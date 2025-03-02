from langchain.agents import tool
import random
from datetime import datetime

@tool
def ecommerce_search(query: str, price_range: tuple = None, size: str = None):
    """
    Search for products that match the query, price constraints, and size.
    """
    # Expanded mock product list with additional attributes including in_stock
    mock_products = [
        {"name": "Floral Skirt", "price": 35, "size": "S", "in_stock": True, "site": "Site A"},
        {"name": "White Sneakers", "price": 65, "size": "8", "in_stock": True, "site": "Site B"},
        {"name": "Casual Denim Jacket", "price": 80, "size": "M", "in_stock": True, "site": "SiteA"},
        {"name": "Blue Jeans", "price": 55, "size": "L", "in_stock": True, "site": "Site C"},
        {"name": "Cocktail Dress", "price": 120, "size": "M", "in_stock": False, "site": "SiteB"}
    ]
    results = []
    for p in mock_products:
        if query.lower() in p["name"].lower():
            # Check price constraint if provided
            if price_range and (price_range[0] <= p["price"] <= price_range[1]):
                results.append(p)
            # Check size if provided
            if size and p["size"].lower() != size.lower():
                continue
            results.append(p)
    return results if results else ["No matching products found"]

@tool
def get_today_date_and_day():
    """
    Returns today's date and the day of the week.
    """
    today = datetime.now()
    date_str = today.strftime("%Y-%m-%d")
    day_str = today.strftime("%A")
    return {"date": date_str, "day": day_str}

@tool
def shipping_estimator(product_name: str, location: str, desired_delivery: str, price_limit: float = None):
    """
    Returns mock shipping details including feasibility, cost, estimated delivery date, and shipping status.
    """
    # Simulate shipping feasibility based on location
    if not location:
        location="Hyderabad"
    feasible_locations = ["New York", "Los Angeles", "Chicago", "Houston","Hyderabad"]
    is_location_feasible = location in feasible_locations

    # Simulate shipping cost and estimated delivery days
    shipping_cost = random.randint(5, 20)
    estimated_days = random.randint(1, 5)  # simulate quick shipping for deadline scenarios

    # Calculate estimated delivery date
    from datetime import datetime, timedelta
    estimated_delivery_date = (datetime.now() + timedelta(days=estimated_days)).strftime("%Y-%m-%d")

    # Check if the desired delivery date is feasible
    desired_date_obj = datetime.strptime(desired_delivery, "%Y-%m-%d")
    is_date_feasible = desired_date_obj >= datetime.now() + timedelta(days=estimated_days)

    # Overall feasibility check
    is_feasible = is_location_feasible and is_date_feasible

    return {
        "feasibility": "Feasible" if is_feasible else "Not feasible",
        "cost": f"${shipping_cost}",
        "estimated_delivery": estimated_delivery_date,
        "status": f"Shipping available to your location :{location}" if is_feasible else "Shipping not available"
    }

@tool
def discount_checker(base_price: float, promo_code: str):
    """
    Adjust the base price based on the provided promo code.
    """
    promo_discounts = {"SAVE10": 0.10, "FREESHIP": 5, "WELCOME20": 0.20}
    discount = promo_discounts.get(promo_code, 0)
    if isinstance(discount, float):
        final_price = base_price * (1 - discount)
    else:
        final_price = max(0, base_price - discount)
    return {"final_price": final_price, "discount_applied": promo_code if promo_code in promo_discounts else "None"}

@tool
def competitor_price_comparison(product_name: str, current_site: str, current_price: float):
    """
    Compare current product price with competitor prices from different sites.
    """
    mock_prices = {
        "casual denim jacket": {"SiteA": 80, "SiteB": 75, "SiteC": 78},
        "floral skirt": {"SiteA": 35, "SiteB": 40, "SiteC": 38},
        "white sneakers": {"SiteA": 70, "SiteB": 65, "SiteC": 68},
        "blue jeans": {"SiteA": 55, "SiteB": 60, "SiteC": 53},
    }
    # Get the comparison dictionary for the product (case-insensitive lookup)
    comparison = mock_prices.get(product_name.lower(), "No price comparison available")
    if isinstance(comparison, dict):
        # Filter to show only sites offering a lower price than the current price
        better_deals = {site: price for site, price in comparison.items() if price < current_price}
        return better_deals if better_deals else "No better deals found"
    return comparison

@tool
def return_policy_checker(site: str):
    """
    Provide return policy details for a given e-commerce site.
    """
    mock_policies = {
        "SiteA": "30-day return policy with free returns.",
        "SiteB": "30-day hassle-free return policy with free return shipping.",
        "SiteC": "15-day return policy with a restocking fee."
    }
    return mock_policies.get(site, "Return policy not available.")

