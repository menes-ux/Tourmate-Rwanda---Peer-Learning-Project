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