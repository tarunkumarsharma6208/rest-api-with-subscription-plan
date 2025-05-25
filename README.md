# 🛍️ Product Subscription API with Django

A Django-based application that allows users to subscribe to various plans and access products with an API usage limit system. Ideal for SaaS-based platforms or API monetization systems.

---

## 🚀 Features

- Categorized products listing
- Subscription plans with usage limits
- User-specific API hit tracking
- Auto-expiry of subscriptions based on usage
- Admin integration via Django admin panel

---

## 🧱 Models Overview

### 🔹 Category
Represents product categories.

| Field | Type |
|-------|------|
| name  | CharField |

### 🔹 Product
Product under a category.

| Field | Type |
|-------|------|
| name        | CharField |
| description | CharField |
| price       | DecimalField |
| category    | ForeignKey to `Category` |

### 🔹 Plan
Subscription plan a user can choose.

| Field | Type |
|-------|------|
| name   | CharField |
| price  | DecimalField |
| limit  | PositiveIntegerField |

### 🔹 Subscription
Ties a user to a plan and tracks API usage.

| Field      | Type |
|------------|------|
| plan       | ForeignKey to `Plan` |
| user       | ForeignKey to `User` |
| api_limit  | PositiveIntegerField |
| api_usage  | PositiveIntegerField |
| is_expire  | BooleanField |

---

## 🛠️ Setup Instructions

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/product-subscription-api.git
   cd product-subscription-api
