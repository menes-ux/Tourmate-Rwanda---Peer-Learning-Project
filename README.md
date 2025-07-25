# Tourmate-Rwanda---Peer-Learning-Project

This is project that helps foreigners in Rwanda to view cheap tourist site.

### Features

1. Users can view all the tourist sites
2. Users can register to be a tour guid
3. Admin can add a cab to the database
4. Admin can add Tourist sites
5. User can book a tour

## How to run the code

1. Create .env file on the root directory then add the Database url

```
DATABASE_URL=postgresql://neondb_owner:npg_lybi40rtNHOV@ep-weathered-hat-adn964rx.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require

```

2. Create a virtual environment

```
python3 -m venv venv
```

3. Active it after creating

```
source venv/bin/activate
```

4. Install the requirements file

```
pip install -r requirements.txt

```

5. Run the main script

```
python3 main.py
```

#### when you the code you will be prompt with these options below.

What do you want to do today?
1: View All Tourist Sites
2: Register as a Tour Guide
3: Book a Tour
4: Transactions
5: Add New Site (Admin)
6: Add New Cab (Admin)
7: Exit

1. Option 1 will display the whole tourist site we have partnered with
2. Option 2 will prompt you to register as a tour guide
3. Option 3 will ask you to book a tour. It will ask you to login with email and password, if you are not registered it will ask the you to register.

> > Booking Options:

1. New Booking (Login Required)
2. View Booking
3. Complete Booking
4. Back to Main Menu

if you chose New Booking you will be asked to login with email and password, then enter **Site Code**, you will need to **View All Tourist Sites** on the main menu to see the site code of each tourist site.
After booking you will be asked if you want to pay, yes/no, if you type yes you wounld be asked to add the book code. Just copy the book code that was printed out after book and put it.

4. Transactions is on process... (still working on it)
5. You will be asked to upload a site. (This is for Admin)
6. You will be asked to add a cab (This is for Admin)
