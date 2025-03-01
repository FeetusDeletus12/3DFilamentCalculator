import webbrowser

def open_filament_links():
    links = {
        "Amazon": "https://www.amazon.com/s?k=3d+printer+filament",
        "MatterHackers": "https://www.matterhackers.com/store/c/3d-printer-filament",
        "Prusa": "https://www.prusa3d.com/category/filaments/",
        "Polymaker": "https://www.polymaker.com/product-category/filaments/",
        "Overture": "https://overture3d.com/collections/all"
    }

    print("\nHere are some common filament suppliers:")
    for name, url in links.items():
        print(f"- {name}: {url}")

    open_links = input("\nWould you like to open these links in your browser? (yes/no): ").strip().lower()
    if open_links == "yes":
        for url in links.values():
            webbrowser.open(url)

def calculate_filament_cost():
    # Get user inputs
    total_cost = float(input("Enter the total cost of the filament spool ($): "))
    
    print("\nBefore entering the filament weight, here are some common suppliers.")
    open_filament_links()

    total_weight = float(input("\nEnter the total filament weight (g): "))
    used_weight = float(input("Enter the amount of filament used (g): "))

    # Calculate cost per gram
    cost_per_gram = total_cost / total_weight

    # Calculate cost of the used filament
    used_cost = cost_per_gram * used_weight

    # Display the result
    print(f"\nCost per gram: ${cost_per_gram:.4f}")
    print(f"Cost of {used_weight}g filament: ${used_cost:.2f}")

# Run the function
calculate_filament_cost()
