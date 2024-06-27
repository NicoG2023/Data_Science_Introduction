import json
import random
from faker import Faker

fake = Faker()

# Predefined mapping of countries to cities
countries_cities = {
    'USA': ['New York', 'Los Angeles', 'Chicago', 'San Francisco', 'Miami', 'Seattle', 'Austin', None],
    'Germany': ['Berlin', 'Munich', 'Frankfurt', 'Hamburg', 'Cologne', 'Stuttgart', None],
    'Japan': ['Tokyo', 'Osaka', 'Kyoto', 'Sapporo', 'Nagoya', 'Fukuoka', None],
    'Canada': ['Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Ottawa', 'Edmonton', None],
    'UK': ['London', 'Manchester', 'Birmingham', 'Glasgow', 'Liverpool', 'Bristol', None],
    'Australia': ['Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Canberra', None],
    'France': ['Paris', 'Marseille', 'Lyon', 'Toulouse', 'Nice', 'Nantes', None],
    'India': ['Mumbai', 'Delhi', 'Bangalore', 'Hyderabad', 'Chennai', 'Kolkata', None],
    'Brazil': ['São Paulo', 'Rio de Janeiro', 'Salvador', 'Brasília', 'Fortaleza', 'Belo Horizonte', None],
    'South Korea': ['Seoul', 'Busan', 'Incheon', 'Daegu', 'Daejeon', 'Gwangju', None],
    'China': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu', 'Xi\'an', None],
    'Russia': ['Moscow', 'Saint Petersburg', 'Novosibirsk', 'Yekaterinburg', 'Kazan', 'Nizhny Novgorod', None],
    'Italy': ['Rome', 'Milan', 'Naples', 'Turin', 'Palermo', 'Genoa', None],
    'Spain': ['Madrid', 'Barcelona', 'Valencia', 'Seville', 'Zaragoza', 'Malaga', None],
    'Mexico': ['Mexico City', 'Guadalajara', 'Monterrey', 'Puebla', 'Tijuana', 'Cancun', None]
}

# Products and sample comments
products = [
    'Laptop', 'Tablet', 'Smartphone', 'Monitor', 
    'Gaming Console', 'Smart Watch', 'E-Reader', 
    'Desktop Computer', 'Graphics Card', 'External Hard Drive', 
    'SSD', 'USB Flash Drive', 'Wireless Router', 
    'Noise Cancelling Headphones', 'Bluetooth Speaker', 
    'Smart Home Assistant', 'VR Headset', 'Drone', 
    '3D Printer', 'Digital Camera', 'Action Camera', 
    'Smart Thermostat', 'Fitness Tracker', 'Wireless Charger', 
    'Portable Projector', 'Smart Lock', 'Streaming Stick'
]

product_comments = {
    'Laptop': [
        'Incredible battery life and performance.',
        'Sleek design, but gets hot under heavy use.',
        'Perfect for both work and gaming.'
    ],
    'Tablet': [
        'Great for reading and streaming videos.',
        'Light and easy to carry around.',
        'Could use more accessories.'
    ],
    'Smartphone': [
        'Amazing camera quality, especially in low light.',
        'Battery lasts all day with moderate use.',
        'Wish it had more storage options.'
    ],
    'Monitor': [
        'Colors are vibrant and the display is sharp.',
        'Great for gaming with low latency.',
        'Stand could be more adjustable.'
    ],
    'Gaming Console': [
        'Excellent game selection and performance.',
        'Quiet operation, even during intense gameplay.',
        'Controller battery life could be better.'
    ],
    'Smart Watch': [
        'Tracks fitness activity accurately.',
        'Notifications are handy, but can be overwhelming.',
        'Battery life is good, but not great.'
    ],
    'E-Reader': [
        'Makes reading at night comfortable and easy.',
        'Battery lasts weeks on a single charge.',
        'Wish it supported more file formats natively.'
    ],
    'Desktop Computer': [
        'Powerful performance for all my computing needs.',
        'Easy to upgrade and customize.',
        'Takes up a lot of space.'
    ],
    'Graphics Card': [
        'Can handle most games at high settings.',
        'Runs cool and quiet under load.',
        'Pricey, but worth it for the performance.'
    ],
    'External Hard Drive': [
        'Compact and easy to carry.',
        'Transfer speeds are fast and reliable.',
        'Feels a bit fragile.'
    ],
    'SSD': [
        'Significantly improved my computer\'s boot time.',
        'Reliable and fast storage solution.',
        'Capacity can get expensive.'
    ],
    'USB Flash Drive': [
        'Convenient for quick file transfers.',
        'Small and portable, but easy to lose.',
        'Write speeds could be faster.'
    ],
    'Wireless Router': [
        'Strong and stable Wi-Fi coverage throughout my home.',
        'Setup was a breeze.',
        'Admin interface could be more user-friendly.'
    ],
    'Noise Cancelling Headphones': [
        'Effectively blocks out background noise.',
        'Sound quality is top-notch.',
        'Can be uncomfortable during long listening sessions.'
    ],
    'Bluetooth Speaker': [
        'Great sound quality for its size.',
        'Battery lasts all day.',
        'Water-resistant feature is a plus.'
    ],
    'Smart Home Assistant': [
        'Makes controlling smart home devices easy.',
        'Voice recognition works well.',
        'Concerns about privacy and data security.'
    ],
    'VR Headset': [
        'Immersive gaming and media experience.',
        'Setup can be complex.',
        'Requires a lot of space for the best experience.'
    ],
    'Drone': [
        'Takes amazing aerial photos and videos.',
        'Battery life limits flight time.',
        'Learning curve for beginners.'
    ],
    '3D Printer': [
        'Great for prototyping and hobby projects.',
        'Setup and calibration can be time-consuming.',
        'Material costs can add up.'
    ],
    'Digital Camera': [
        'Excellent image quality and features.',
        'Compact and easy to carry on trips.',
        'Lenses and accessories can be expensive.'
    ],
    'Action Camera': [
        'Durable and waterproof, great for adventure sports.',
        'Battery drains quickly with continuous use.',
        'Wide-angle lens captures stunning perspectives.'
    ],
    'Smart Thermostat': [
        'Easy to control from my phone.',
        'Saves on heating and cooling costs.',
        'Installation was a bit tricky.'
    ],
    'Fitness Tracker': [
        'Motivates me to stay active.',
        'Tracks a wide range of activities.',
        'Accuracy can vary depending on the activity.'
    ],
    'Wireless Charger': [
        'Convenient, just drop and charge.',
        'Charging speed is slower than wired.',
        'Needs precise placement to charge effectively.'
    ],
    'Portable Projector': [
        'Turns any room into a home theater.',
        'Battery life could be longer.',
        'Brightness is adequate for dimly lit rooms.'
    ],
    'Smart Lock': [
        'Adds convenience and security to my home.',
        'Easy to share access with family and guests.',
        'Setup was more complicated than expected.'
    ],
    'Streaming Stick': [
        'Turns any TV into a smart TV.',
        'Easy to set up and use.',
        'Sometimes lags with high-resolution content.'
    ]
}

def get_random_datetime_or_none():
    # Low probability for None
    return fake.date_time_this_decade() if random.choices([True, False], weights=[98, 2])[0] else None

def get_random_attention_time_or_none():
    # Low probability for None
    return random.uniform(5, 150) if random.choices([True, False], weights=[95, 5])[0] else None

def get_country_city():
    country = random.choice(list(countries_cities.keys()))
    city = random.choice(countries_cities[country])
    return country, city

comments = []
for i in range(1000000):
    product = random.choice(products)
    country, city = get_country_city()
    comment_text = random.choice(product_comments.get(product, ['No comment available.']))
    comment = {
        "code": fake.bothify(text='???-#######'),
        "client": fake.name(),
        "product": product,
        "date_time": get_random_datetime_or_none(),
        "attention_time": get_random_attention_time_or_none(),
        "comment": comment_text,
        "country_of_origin": country,
        "city": city
    }
    # Convert datetime to string if not None
    if comment['date_time']:
        comment['date_time'] = comment['date_time'].strftime('%Y-%m-%d %H:%M:%S')
    comments.append(comment)

# Write to JSON file
with open('call_center_comments.json', 'w') as f:
    json.dump(comments, f, indent=4)