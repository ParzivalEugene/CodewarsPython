"""
Simple code that allows me to name my files properly
"""
title = input("Insert title of kata: ")
print(title.replace(" ", "_").replace(":", "-").replace("?", ""))