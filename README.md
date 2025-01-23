# Fitora: Virtual Try-On E-Commerce Platform :shopping: :sparkles:

Welcome to the **Fitora** repository! This project is an AI-powered virtual try-on platform designed to enhance the online shopping experience by allowing users to virtually try on clothes. Fitora combines cutting-edge technology and seamless integration with popular e-commerce platforms for a personalized and engaging shopping journey.

---

## Key Features :star2:

- **AI-Powered Virtual Try-On**: 
  Advanced machine learning algorithms for image recognition and fitting to enable users to virtually try on clothes.
  
- **Product Integration**: 
  Real-time product data fetched from Amazon, Flipkart, and Meesho using the Amazon Product Listing (PAAPI) API.
  
- **Personalized User Engagement**:
  Email, WhatsApp, and push notifications enhance user engagement, increasing website traffic and conversion rates.
  
- **Admin Dashboard**: 
  Easy-to-use dashboard for managing products, inventory, pricing, and user engagement metrics.

---

## Tech Stack :computer: 

- **Backend**: Python, RESTful APIs
- **Frontend**: React.js
- **AI/ML**: Machine Learning, HuggingFace
- **Infrastructure**: AWS
- **Notifications**: Email, WhatsApp, Push Notifications

---

## Getting Started

Follow the instructions below to get started with the Fitora project:

## 1 **Add SSH Key to GitHub Account:** 
Before cloning the repository, ensure you have set up SSH key authentication with GitHub.

## 2 **Install Docker:(Not Required)** 
Make sure Docker is installed on your system. If not,
> [!TIP]
> download and install it from [here](https://www.docker.com/get-started).
    
## 3 . create a vertual env.
> [!IMPORTANT]
> Before proceeding, it's recommended to set up a Python virtual environment for the project.

## 4. **Clone the Repository:** 
Clone this repository to your local machine using the following command: 
 
  
  ```
 git clone https://github.com/Ashish8329/FiTora.git
```

## 5.  Navigate to Project Directory: 
Go to the directory where you cloned the repository.
 
## 6.  Build and Run Docker: 
Ensure Docker is running in the background. Navigate to the main directory of the project and run:
##4. Navigate to Project Directory:
Go to the directory where you cloned the repository.
> [!NOTE]
> # For the first time

  ```
  docker-compose up --build   
```
Or
> [!NOTE]
> # For subsequent runs
```
docker-compose up   
```

## 7. Create Superuser: 
After the project is successfully set up, create a superuser using the following command:
```
python3 manage.py createsuperuser 
```
Follow the prompts to set up the superuser credentials. 

## 8. Explore the Fitora Project: :sparkles:'
:point_right: **Congratulations**:balloon:!:tada::tada: Your Fitora project is now ready to explore.:confetti_ball:	:balloon: :point_left:
