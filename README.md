# API Carsharing Service

---

### 🎯Purpose

Realize REST API of carsharing, for convenient car rental.

---

### 📝Description

**The project contains the following user functionality:**  
1) Add the ability to register (using JWT tokens), log out, modify and retrieve account information;
2) Add, modify and delete transportation;
3) Receive information about available leased transports, lease a transport and end a transport lease;
4) Receive the history of your vehicle rentals;
5) Obtain the history of a vehicle rental by its ID;
6) Permissions to work with transport: only authorized users can add transport, only its owner can change/remove transport;
7) Permissions to work with leases: only the lessee and the owner of the transport can receive information about the lease, only the owner of the transport can receive the history of the lease of the transport, only the authorized user can receive the history of his leases, you can not rent your own transport, only the lessee can end the lease;

**Project contains the following administrator functionality:**
1) Getting the list of all accounts and information about one account by its ID;
2) Creating, modifying and deleting an account by administrator;
3) Getting a list of all vehicles and getting information about a vehicle by its ID;
4) Creation, modification, deletion of a vehicle;
5) Creating, modifying, deleting and finalizing a lease;
6) Obtaining user's rental history by user ID;
7) Obtaining the rental history of a vehicle by its ID;

---

### 🛠️Stack

**Languages**: Python;  
**Frameworks**: Django, Django REST Framework;  
**Libraries**: djoser, psycopg2, drf-nested-routers, python-dotenv, drf-yasg, geopy, simpleJWT, django-filter;  
**Database**: PostgreSQL;
**Tools**: Docker, docker-compose.

---

### ⚙️Installation

---

1) **Clone the repository**: ```git clone https://github.com/shoksdev/simple_buy.git```  
2) **Go to the project folder**: ```cd volga_it```  
3) **Start the project with superuser creation**: ```docker-compose run django python manage.py createsuperuser```  
4) **Bring the project**: ```docker-compose up```  

---

### 📙Guidelines for use

Go to http://127.0.0.1:8000/swagger/ for a better test of API endpoints.

---

#### Thank you very much for taking the time to share this repository and my profile in general. All the best!
