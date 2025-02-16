
countries_and_capitals = {
    "United States": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}


fruits_and_colors = {
    "Apple": "Red",
    "Banana": "Yellow",
    "Grapes": "Purple"
}

merged_dic = {**countries_and_capitals, **fruits_and_colors}

print(merged_dic)