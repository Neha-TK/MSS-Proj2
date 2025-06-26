# 📝 Flask To-Do API

A simple RESTful API built using **Flask** that lets you manage a to-do list.  
This project allows users to **view**, **add**, **update**, and **delete** tasks using standard HTTP methods. It’s perfect for beginners to understand how APIs work with Python and Flask.

---

## 📋 Features

- `GET /todo` — Fetch all to-do items  
- `POST /todo` — Add a new item to the list  
- `DELETE /todo/delete/<item_id>` — Delete an item by its index  
- `PUT /todo/update/<item_id>` — Update an item by its index  

---

## 🧾 Sample To-Do List

```json
["write", "read", "code", "test"]
