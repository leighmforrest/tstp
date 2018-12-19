# Philadelphia (I live here), Munchen, London, New York, Paris
cities_visited = [
            (39.97977, -75.11602),
            (48.138874, 11.560239),
            (51.526356, -0.124455),
            (40.73952, -74.008934),
            (48.88259, 2.341526)
        ]

# Added: Malmo, Zurich, San Diego, Montreal
dream_job_cities = [
                        (55.613255, 12.97638),
                        (47.37861, 8.54),
                        (32.7978, -117.2403),
                        (45.500465, -73.56713)
                   ]

print("Cities Visited:",cities_visited)

new_list = (cities_visited + dream_job_cities)
print("Cities Visited plus Places I Want to Work In:")
print(new_list)
