import customtkinter as ctk
from tkinter import messagebox
import json
import os
import random
from matplotlib import pyplot as plt

#def on_login_pressed():
#    username = username_entry.get()
#    password = password_entry.get()
#    role = role_combobox.get()

#    if username == "user" and password == "password" and role == "User":
#        open_candidate_selection(username)
#    elif username == "admin" and password == "admin123" and role == "Administrator":
#        open_admin_dashboard(username)
#    else:
#        messagebox.showerror("Login Failed", "Invalid credentials or role selection.")

def load_user_data_from_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data.get("user", [])
    except FileNotFoundError:
        return []

class UserData:
    def __init__(self):
        self.user = []
        self.password = []
        self.email = []

    def load_from_json(self, filename):
        if os.path.isfile(filename):
            with open(filename, "r") as file:
                data = json.load(file)
                self.user = data.get("user", [])
                self.password = data.get("password", [])
                self.email = data.get("email", [])
                return data
        else:
            print(f"The file {filename} does not exist. Creating a new file.")
            default_data = {
                "user": [],
                "password": [],
                "email": []
            }
            with open(filename, "w") as json_file:
                json.dump(default_data, json_file, indent=4)
            print(f"New file {filename} created.")

    def save_to_json(self, filename):
        data = {
            "user": self.user,
            "password": self.password,
            "email": self.email
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def authenticate_user(self, username, password):
        # Check if the entered username exists
        if username in self.user:
            # Get the index of the username
            index = self.user.index(username)
            # Check if the stored password at the same index matches the entered password
            if self.password[index] == password:
                return True
        return False


class Register(UserData):
    def __init__(self, root):
          super().__init__()
          self.root = root
          self.root.title("Register")
          self.data = UserData()
          self.data.load_from_json("user_data.json")

    def open_registration(self):
          self.reg_window = ctk.CTkToplevel(self.root)
          self.reg_window.title("Register")
          self.reg_window.geometry("400x300")

          # Username entry
          self.username_entry = ctk.CTkEntry(self.reg_window, placeholder_text="Username", width=300, height=40)
          self.username_entry.grid(row=0, column=1, padx=20, pady=10)
          ctk.CTkLabel(self.reg_window, text="Username:").grid(row=0, column=0, sticky="e")

          # Password entry
          self.password_entry = ctk.CTkEntry(self.reg_window, placeholder_text="Password", show="*", width=300,
                                             height=40)
          self.password_entry.grid(row=1, column=1, padx=20, pady=10)
          ctk.CTkLabel(self.reg_window, text="Password:").grid(row=1, column=0, sticky="e")

          # Confirm password entry
          self.confirm_password_entry = ctk.CTkEntry(self.reg_window, placeholder_text="Confirm Password", show="*",
                                                     width=300, height=40)
          self.confirm_password_entry.grid(row=2, column=1, padx=20, pady=10)
          ctk.CTkLabel(self.reg_window, text="Confirm Password:").grid(row=2, column=0, sticky="e")

          # Email entry
          self.email_entry = ctk.CTkEntry(self.reg_window, placeholder_text="Email", width=300, height=40)
          self.email_entry.grid(row=3, column=1, padx=20, pady=10)
          ctk.CTkLabel(self.reg_window, text="Email:").grid(row=3, column=0, sticky="e")

          # Submit button
          self.submit_button = ctk.CTkButton(self.reg_window, text="Submit", command=self.submit_registration)
          self.submit_button.grid(row=4, column=0, columnspan=2, pady=20, sticky="ew")

    def submit_registration(self):
          username = self.username_entry.get()
          password = self.password_entry.get()
          confirm_password = self.confirm_password_entry.get()
          email = self.email_entry.get()

          self.load_from_json("user_data.json")

          # Validate input (e.g., check if passwords match)
          if password != confirm_password:
              messagebox.showerror("Error", "Passwords do not match.")
              return
          elif email == "" or username == "" or password == "":
              messagebox.showerror("Error", "Input all required information")
              return
          messagebox.showinfo("Registration Complete", f"Registered {username} with email {email}.")
          self.reg_window.destroy()

          # Append the new user data to the respective lists
          self.user.append(username)
          self.password.append(password)
          self.email.append(email)

          # Save data to JSON
          try:
              self.save_to_json("user_data.json")
              print("Data saved successfully!")
          except Exception as e:
              print(f"Error saving data: {str(e)}")

          # Show a success message (you can use a messagebox here)
          print("Registration successful!")

def on_login_pressed():
    username = username_entry.get()
    password = password_entry.get()
    role = role_combobox.get()

    user_data = UserData()
    user_data.load_from_json("user_data.json")

    if user_data.authenticate_user(username, password):
        if role == "User":
            open_candidate_selection(username)
    elif username == "admin" and password == "admin123" and role == "Administrator":
            open_admin_dashboard(username)
    else:
        messagebox.showerror("Login Failed", "Invalid credentials.")

def open_candidate_selection(username):
    selection_window = ctk.CTkToplevel(root)
    selection_window.title("Select Candidate")
    selection_window.geometry("600x400")

    selection_frame = ctk.CTkFrame(selection_window)
    selection_frame.pack(side="left", fill="both", expand=True)

    info_frame = ctk.CTkFrame(selection_window)
    info_frame.pack(side="right", fill="both", expand=True)

    ctk.CTkLabel(selection_frame, text=f"Hello, {username}! Please select a candidate:").pack(pady=20)

    candidates = {
        "John M": "Details about Candidate A: Democrat, more students aids",
        "Paul O": "Details about Candidate B: Republic, banned guns.",
        "Sam S": "Details about Candidate C: Democrat, make health care free.",
        "Nook H": "Details about Candidate D: Republic, let more immigrants in."
    }

    info_text = ctk.CTkLabel(info_frame, text="", wraplength=250)
    info_text.pack(pady=20)

    vote_button = ctk.CTkButton(info_frame, text="Vote", state="disabled",
                                command=lambda: cast_vote(selected_candidate.get(), selection_window, username))
    vote_button.pack(pady=10)

    selected_candidate = ctk.StringVar(value="")  # Track the selected candidate

    for candidate, details in candidates.items():
        button = ctk.CTkButton(selection_frame, text=candidate,
                               command=lambda c=candidate, d=details: update_info(info_text, vote_button, c, d, selected_candidate))
        button.pack(pady=10)

class VoteManager:
    def __init__(self):
        self.vote_data = {}


    def load_from_json1(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print(f"File {filename} not found. Creating a new one.")
            default_data = {
                "John M": [],
                "Paul O": [],
                "Sam S": [],
                "Nook H": []
            }
            self.save_to_json1(default_data)
            return default_data

    def save_to_json1(self, filename, data):
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def cast_vote(self, candidate, username):
        self.vote_data[candidate].append(username)
        self.save_to_json1(self.vote_data)


def update_info(info_label, vote_button, candidate, details, selected_candidate):
    info_label.configure(text=f"{candidate}: {details}")
    selected_candidate.set(candidate)
    vote_button.configure(state="normal")  # Enable the vote button after a candidate is selected

def cast_vote(candidate, window, username):
    messagebox.showinfo("Vote Cast", f"You have voted for {candidate}.")
    window.destroy()  # Optionally close the selection window after voting
    vote_data[candidate].append(username)
    display_vote_counts()

    # Save data to JSON
    try:
        VoteManager().save_to_json1("candidate_vote.json", vote_data)
        print("Data saved successfully!")
    except Exception as e:
        print(f"Error saving data: {str(e)}")

vote_data = {
    "John M": [],
    "Paul O": [],
    "Sam S": [],
    "Nook H": []
}



def open_admin_dashboard(username):
    dashboard_window = ctk.CTkToplevel(root)
    dashboard_window.title("Admin Dashboard")
    dashboard_window.geometry("400x300")

    welcome_label = ctk.CTkLabel(dashboard_window, text=f"Welcome, {username}! This is the admin dashboard.")
    welcome_label.pack(pady=20)

    stats_button = ctk.CTkButton(dashboard_window, text="Open Stats Page", command=open_stats_page)
    stats_button.pack(pady=10)

    stats_button = ctk.CTkButton(dashboard_window, text="User information", command=open_user_info_page)
    stats_button.pack(pady=10)

    stats_button = ctk.CTkButton(dashboard_window, text="Simulation", command=open_sim_page)
    stats_button.pack(pady=10)

def open_stats_page():
    plt.show()


def open_user_info_page():
    user_info_window = ctk.CTkToplevel(root)
    user_info_window.title("User Information")
    user_info_window.geometry("600x400")

    # Scrollable region using a canvas and a frame


    # Display each user's information
    for i, username in enumerate(user_data.user):
        user_label = ctk.CTkLabel(user_info_window, text=f"User {i+1}: Username: {username}, Email: {user_data.email[i]}")
        user_label.pack(pady=10, padx=10, fill='x')

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i][1] > R[j][1]:  # Change '<' to '>' for descending order
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def display_vote_counts():
    for candidate, votes in vote_data.items():
        print(f"{candidate}: {len(votes)} votes")

#def submit_registration(username, password, confirm_password, email, reg_window):
#    if password != confirm_password:
#        messagebox.showerror("Error", "Passwords do not match.")
#        return
#    messagebox.showinfo("Registration Complete", f"Registered {username} with email {email}.")
#    reg_window.destroy()

root = ctk.CTk()

root.title("Login Interface")
root.geometry("400x300")

  # Username Entry
username_entry = ctk.CTkEntry(root, placeholder_text="Username", width=300, height=40)
username_entry.grid(row=0, column=1, padx=20, pady=10, columnspan=2)
ctk.CTkLabel(root, text="Username:").grid(row=0, column=0, sticky="e")

  # Password Entry
password_entry = ctk.CTkEntry(root, show="*", placeholder_text="Password", width=300, height=40)
password_entry.grid(row=1, column=1, padx=20, pady=10, columnspan=2)
ctk.CTkLabel(root, text="Password:").grid(row=1, column=0, sticky="e")

  # Role Combobox
role_combobox = ctk.CTkComboBox(root, values=["User", "Administrator"], width=300, height=40)
role_combobox.set("User")  # Default to 'User'
role_combobox.grid(row=2, column=1, padx=20, pady=10, columnspan=2)
ctk.CTkLabel(root, text="Role:").grid(row=2, column=0, sticky="e")

  # Login Button
login_button = ctk.CTkButton(root, text="Login", command=on_login_pressed)
login_button.grid(row=3, column=0, columnspan=2, pady=20, sticky="ew")

res = Register(root)

  # Register Button
register_button = ctk.CTkButton(root, text="Register", command=res.open_registration)
register_button.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

def open_sim_page():
    stats_window = ctk.CTkToplevel(root)
    stats_window.title("This page is for simulation purpose")
    stats_window.geometry("600x400")
    stats_label = ctk.CTkLabel(stats_window, text="Here is some of the ops:")
    stats_label.pack(pady=20)

    stats_button = ctk.CTkButton(stats_window, text="If there is a gun murder", command=simulate_gun_murder_event)
    stats_button.pack(pady=10)

    stats_button = ctk.CTkButton(stats_window, text="If there is a war happening at another country", command=simulate_War)
    stats_button.pack(pady=10)

    stats_button = ctk.CTkButton(stats_window, text="If there is a disease", command=simulate_disease)
    stats_button.pack(pady=10)

    stats_button = ctk.CTkButton(stats_window, text="If there the payment is too low", command=simulate_payment)
    stats_button.pack(pady=10)

def display_vote_results():
    result_window = ctk.CTkToplevel(root)
    result_window.title("Simulation Results")
    result_window.geometry("400x300")

    # Collect data in a sortable form
    results = [(candidate, len(votes)) for candidate, votes in random_votes.items()]
    merge_sort(results)  # Sort results in descending order by vote count

    header_label = ctk.CTkLabel(result_window, text="Election Results After Simulation (Sorted):")
    header_label.pack(pady=10)

    # Display sorted results
    for candidate, vote_count in results:
        result_label = ctk.CTkLabel(result_window, text=f"{candidate}: {vote_count} votes")
        result_label.pack(pady=5)


random_votes = {}
def simulate_gun_murder_event():
    # Dictionary to store random vote counts for this simulation

    for key in random_votes:
        random_votes[key] = []

    # Randomly generate votes for each candidate
    total_votes = 100  # Total votes to distribute in this simulation
    votes_A = random.randint(0, total_votes // 4)  # Reduce the pool for other candidates
    votes_C = random.randint(0, total_votes // 4)
    votes_D = random.randint(0, total_votes // 4)

    # Ensure Candidate B always wins in this simulation batch
    votes_B = total_votes - (votes_A + votes_C + votes_D)  # Rest of the votes go to Candidate B

    # Add the new votes to the existing totals
    random_votes["Candidate A"] = ['user'] * votes_A
    random_votes["Candidate B"] = ['user'] * votes_B
    random_votes["Candidate C"] = ['user'] * votes_C
    random_votes["Candidate D"] = ['user'] * votes_D


    messagebox.showinfo("Simulation",
                        "Additional votes have been randomly generated for a gun murder event. Candidate B has the most votes in this batch.")
    display_vote_results()  # Optionally open a new window to show the updated results

def simulate_War():
    # Dictionary to store random vote counts for this simulation

    for key in random_votes:
        random_votes[key] = []

    # Randomly generate votes for each candidate
    total_votes = 100  # Total votes to distribute in this simulation
    votes_A = random.randint(0, total_votes // 4)  # Reduce the pool for other candidates
    votes_C = random.randint(0, total_votes // 4)
    votes_B = random.randint(0, total_votes // 4)

    # Ensure Candidate B always wins in this simulation batch
    votes_D = total_votes - (votes_A + votes_C + votes_B)  # Rest of the votes go to Candidate B

    # Add the new votes to the existing totals
    random_votes["Candidate A"] = ['user'] * votes_A
    random_votes["Candidate B"] = ['user'] * votes_B
    random_votes["Candidate C"] = ['user'] * votes_C
    random_votes["Candidate D"] = ['user'] * votes_D


    messagebox.showinfo("Simulation",
                        "Additional votes have been randomly generated for a gun murder event. Candidate B has the most votes in this batch.")
    display_vote_results()  # Optionally open a new window to show the updated results

def simulate_disease():
    # Dictionary to store random vote counts for this simulation

    for key in random_votes:
        random_votes[key] = []

    # Randomly generate votes for each candidate
    total_votes = 100  # Total votes to distribute in this simulation
    votes_A = random.randint(0, total_votes // 4)  # Reduce the pool for other candidates
    votes_B = random.randint(0, total_votes // 4)
    votes_D = random.randint(0, total_votes // 4)

    # Ensure Candidate B always wins in this simulation batch
    votes_C = total_votes - (votes_A + votes_B + votes_D)  # Rest of the votes go to Candidate B

    # Add the new votes to the existing totals
    random_votes["Candidate A"] = ['user'] * votes_A
    random_votes["Candidate B"] = ['user'] * votes_B
    random_votes["Candidate C"] = ['user'] * votes_C
    random_votes["Candidate D"] = ['user'] * votes_D


    messagebox.showinfo("Simulation",
                        "Additional votes have been randomly generated for a gun murder event. Candidate B has the most votes in this batch.")
    display_vote_results()  # Optionally open a new window to show the updated results

def simulate_payment():
    # Dictionary to store random vote counts for this simulation

    for key in random_votes:
        random_votes[key] = []

    # Randomly generate votes for each candidate
    total_votes = 100  # Total votes to distribute in this simulation
    votes_B = random.randint(0, total_votes // 4)  # Reduce the pool for other candidates
    votes_C = random.randint(0, total_votes // 4)
    votes_D = random.randint(0, total_votes // 4)

    # Ensure Candidate B always wins in this simulation batch
    votes_A = total_votes - (votes_B + votes_C + votes_D)  # Rest of the votes go to Candidate B

    # Add the new votes to the existing totals
    random_votes["Candidate A"] = ['user'] * votes_A
    random_votes["Candidate B"] = ['user'] * votes_B
    random_votes["Candidate C"] = ['user'] * votes_C
    random_votes["Candidate D"] = ['user'] * votes_D


    messagebox.showinfo("Simulation",
                        "Additional votes have been randomly generated for a gun murder event. Candidate B has the most votes in this batch.")
    display_vote_results()  # Optionally open a new window to show the updated results


try:

    plt.style.use("fivethirtyeight")

    slices = []
    labels = []

    for candidates, votes in VoteManager().load_from_json1("candidate_vote.json").items():
        slices.append(len(votes))
        labels.append(candidates)

    plt.pie(slices, labels=labels, autopct='%1.1f%%')

    plt.title("")
    plt.tight_layout()

except Exception as e:
    pass



if __name__ == "__main__":
    user_data = UserData()
    candidate_vote = VoteManager()

    candidate_vote.load_from_json1("candidate_vote.json")

    user_data.load_from_json("user_data.json")

    display_vote_counts()

    print(vote_data)

    user_data.save_to_json("user_data.json")

      # Load user data from the JSON file (e.g., "user_data.json")
      # Print loaded user data (for verification)
    print("Loaded user data:", user_data.user, user_data.password, user_data.email)

    root.mainloop()
