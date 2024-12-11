import tkinter as tk
from tkinter import messagebox
import clips 

def market_advisor():
    env = clips.Environment()
    env.load("D:/uni/software/New folder/pari.CLP")
    env.reset()

    def recommend_suitable_destination():
        output_text.delete("1.0", tk.END)
        business = business_entry.get()
        if not business:
            messagebox.showwarning("Input Error", "Please enter Business.")
            return
        # Replace this with logic to find the nearest shelter
        env.reset()
        env.assert_string(f"(selected-industry (industry {business}))")
        env.run()
        for function in env.facts():
            print(function)
        for fact in env.facts():
    # Check if the fact matches the `floodrisk` template
             if fact.template.name == "recommended-location":
        # Extract the values of the slots (stationid and risk)
                location = fact["location"]
                suitability_factors = fact["suitability-factors"]

                output_text.insert("1.0", f" {location}: {suitability_factors}\n")

    def license_permit():
        output_text.delete("1.0", tk.END)
        business = business_entry.get()
        if not business:
            messagebox.showwarning("Input Error", "Please enter Business.")
            return
        # Replace this with logic to find the nearest shelter
        env.reset()
        env.assert_string(f"(selected-industry (industry {business}))")
        env.run()
        for function in env.facts():
            print(function)
        for fact in env.facts():
    # Check if the fact matches the `floodrisk` template
             if fact.template.name == "regulatory-requirement":
        # Extract the values of the slots (stationid and risk)
                requirements = fact["requirements"]
                

                output_text.insert("1.0", f" {requirements}\n")

    def funding():
        output_text.delete("1.0", tk.END)
        business = business_entry.get()
        if not business:
            messagebox.showwarning("Input Error", "Please enter Business.")
            return
        # Replace this with logic to find the nearest shelter
        env.reset()
        env.assert_string(f"(selected-industry (industry {business}))")
        env.run()
        for function in env.facts():
            print(function)
        for fact in env.facts():
    # Check if the fact matches the `floodrisk` template
             if fact.template.name == "funding-recommendation":
        # Extract the values of the slots (stationid and risk)
                requirements = fact["sources"]
                

                output_text.insert("1.0", f" Funding Sources are {requirements}\n")
        
       

    # Clear the main window
    for widget in main_window.winfo_children():
        widget.destroy()

    # Create the interface for route protection
    tk.Label(main_window, text="Sri Lankan Market Entry Advisor for Startups", font=("Arial", 18)).pack(pady=10)

    tk.Label(main_window, text="Enter Business type (tech/tourism/retail):").pack(pady=5, anchor="w", padx=10)

    business_entry = tk.Entry(main_window, width=30)
    business_entry.pack(pady=5)

    tk.Button(main_window, text="Recommend Destination", command=recommend_suitable_destination).pack(pady=5)
    tk.Button(main_window, text="Necessary License and Permits", command=license_permit).pack(pady=5)
    tk.Button(main_window, text="Get Funding Sources", command=funding).pack(pady=5)
    

    output_text = tk.Text(main_window, height=10, width=50)
    output_text.pack(pady=10)

    

root = tk.Tk()
root.title("Sri Lankan Market Entry Advisor for Startups")
root.geometry("400x400")

main_window = tk.Frame(root)
main_window.pack(fill="both", expand=True)

# Display the homepage initially
market_advisor()
env = clips.Environment()



# Run the application
root.mainloop()