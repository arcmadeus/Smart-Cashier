import customtkinter as ctk
from sqlalchemy import column

class ShoppingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Cashier App")
        self.configure_gui()

    def configure_gui(self):
        # Get screen dimensions
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # Set the window size dynamically (80% of screen size)
        window_width = int(self.screen_width * 0.7)
        window_height = int(self.screen_height * 0.7)
        x_position = int((self.screen_width - window_width) / 2)
        y_position = int((self.screen_height - window_height) / 2)

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.configure_frames()

    def configure_frames(self):
        # Main frame/Top frame
        self.main_frame = ctk.CTkFrame(
            root, 
            corner_radius=0, 
            width=int(self.screen_width * 0.7),
            height=int(self.screen_height * 0.1),
            border_color="red")
        
        self.main_frame.pack(fill=ctk.BOTH, expand=True)

        # Top bar
        top_frame = ctk.CTkFrame(self.main_frame, corner_radius=0)
        top_frame.pack(side=ctk.TOP, fill=ctk.X)

        group_label = ctk.CTkLabel(top_frame, text="Group Name", font=ctk.CTkFont(size=16, weight="bold"))
        group_label.pack(side=ctk.LEFT, padx=10)

        search_entry = ctk.CTkEntry(top_frame, placeholder_text="Search...")
        search_entry.pack(side=ctk.LEFT, padx=5)

        search_button = ctk.CTkButton(top_frame, text="Search", fg_color="red", text_color="white")
        search_button.pack(side=ctk.LEFT, padx=5)

        cart_button = ctk.CTkButton(top_frame, text="Cart", fg_color=None, text_color="black")
        cart_button.pack(side=ctk.RIGHT, padx=5)

        account_button = ctk.CTkButton(top_frame, text="Account", fg_color=None, text_color="black")
        account_button.pack(side=ctk.RIGHT, padx=5)

        # Button Frames
        self.button_frame = ctk.CTkFrame(
            root, 
            corner_radius=0, 
            width=int(self.screen_width * 0.7),
            height=int(self.screen_height * 0.1),
            border_color="blue")
        self.button_frame.pack(fill=ctk.BOTH, expand=True)

        # Cart Frames
        self.cart_frame = ctk.CTkFrame(
            root, 
            corner_radius=0, 
            width=int(self.screen_width * 0.7),
            height=int(self.screen_height * 0.5),
            border_color="red")
        self.cart_frame.pack(fill=ctk.BOTH, expand=True)


        nav_buttons = ["Home", "Shop", "SCAN", "Calculator", "Contact"]
        for btn in nav_buttons:
            nav_button = ctk.CTkButton(self.button_frame, text=btn, fg_color=None, text_color="black")
            nav_button.pack(side=ctk.RIGHT, padx=5)

        

        # Content frame
        content_frame = ctk.CTkFrame(self.cart_frame, corner_radius=0)
        content_frame.pack(fill=ctk.BOTH, expand=True)

        # Left side (Product List)
        left_frame = ctk.CTkFrame(content_frame, corner_radius=0)
        left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        left_canvas = ctk.CTkCanvas(left_frame, bg="lightgray")
        left_scrollbar = ctk.CTkScrollbar(left_frame, orientation="vertical", command=left_canvas.yview)
        left_scrollable_frame = ctk.CTkFrame(left_canvas, corner_radius=0)

        left_scrollable_frame.bind(
            "<Configure>", lambda e: left_canvas.configure(scrollregion=left_canvas.bbox("all"))
        )

        left_canvas.create_window((0, 0), window=left_scrollable_frame, anchor="nw")
        left_canvas.configure(yscrollcommand=left_scrollbar.set)

        left_canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        left_scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        for i in range(20):  # Example product list
            product_frame = ctk.CTkFrame(left_scrollable_frame, corner_radius=10, fg_color="white")
            product_frame.pack(pady=10, padx=10, fill=ctk.X)

            product_label = ctk.CTkLabel(product_frame, text=f"Product {i+1}", font=ctk.CTkFont(size=14, weight="bold"))
            product_label.pack(anchor="w", padx=5, pady=2)

            barcode_label = ctk.CTkLabel(product_frame, text=f"Barcode: {100000 + i}")
            barcode_label.pack(anchor="w", padx=5)

            stock_label = ctk.CTkLabel(product_frame, text=f"Stock: {10 + i}")
            stock_label.pack(anchor="w", padx=5)

            category_label = ctk.CTkLabel(product_frame, text=f"Category: Category {i%5}")
            category_label.pack(anchor="w", padx=5)

            add_to_cart_button = ctk.CTkButton(product_frame, text="Add to Cart", fg_color="red", text_color="white")
            add_to_cart_button.pack(anchor="e", padx=5, pady=5)

        # Right side (Shopping Cart)
        right_frame = ctk.CTkFrame(content_frame, corner_radius=0)
        right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, padx=10, pady=10)

        right_canvas = ctk.CTkCanvas(right_frame, bg="lightgray")
        right_scrollbar = ctk.CTkScrollbar(right_frame, orientation="vertical", command=right_canvas.yview)
        right_scrollable_frame = ctk.CTkFrame(right_canvas, corner_radius=0)

        right_scrollable_frame.bind(
            "<Configure>", lambda e: right_canvas.configure(scrollregion=right_canvas.bbox("all"))
        )

        right_canvas.create_window((0, 0), window=right_scrollable_frame, anchor="nw")
        right_canvas.configure(yscrollcommand=right_scrollbar.set)

        right_canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True)
        right_scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)

        cart_label = ctk.CTkLabel(right_scrollable_frame, text="Shopping Cart", font=ctk.CTkFont(size=16, weight="bold"))
        cart_label.pack(pady=10)

        # Example cart items
        for i in range(5):
            cart_item_label = ctk.CTkLabel(right_scrollable_frame, text=f"Cart Item {i+1}")
            cart_item_label.pack(anchor="w", padx=10, pady=5)

if __name__ == "__main__":
    root = ctk.CTk()
    app = ShoppingApp()
    root.mainloop()