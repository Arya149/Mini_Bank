# 🏦 Mini Bank Management System

A secure and role-based **banking application** built with **Django** and **MySQL**.  
It allows customers to manage their accounts, employees to assist in daily operations, and managers to oversee the entire banking system.

---

## ✨ Features

### 👤 Customer
- Register a new account (with email verification).
- Receive account number & password via email after approval.
- Change password after first login.
- Login with credentials and view account balance.
- Transfer funds to another account.
- View recent transactions (mini statement).

### 👨‍💼 Employee
- View and update customer information.
- Deposit or withdraw money for customers.
- Transfer funds between accounts.
- Respond to customer service requests.
- View mini statements for customers.

### 🧑‍💻 Manager
- Approve/reject customer and employee account requests.
- Manage customer & employee details.
- Monitor and oversee all transactions.
- Handle service requests at higher level.
- Access complete system overview.

---

## 🛠️ Tech Stack
- **Backend**: Django 5.0.6 (Python 3.12)  
- **Database**: MySQL  
- **Frontend**: Django Templates (HTML, CSS, JS)  
- **Libraries**:
  - `mysqlclient`, `PyMySQL` → Database connectors  
  - `requests`, `cryptography` → Security & API handling   

---

## 🏢 User Roles and Dashboards

### 👤 Customer
- View balance  
- Transfer funds  
- See recent transactions  

### 👨‍💼 Employee
- Manage customer details  
- Process deposits & withdrawals  
- Handle service requests  
- View mini statements  

### 🧑‍💻 Manager
- Approve/reject account requests (customer/employee)  
- Monitor all transactions  
- Manage employees  
- Oversee customer accounts  

---

## ⚙️ Installation Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/mini-bank.git
cd mini-bank
