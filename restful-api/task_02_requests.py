#!/usr/bin/env python3
"""Fetch posts from JSONPlaceholder API and process them."""

import requests
import csv


def fetch_and_print_posts():
    """Fetch posts and print their titles."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        for post in response.json():
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts and save them to 'posts.csv'."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        with open("posts.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(response.json())

        print("Data saved to posts.csv")
