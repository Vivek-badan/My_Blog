from django.shortcuts import render
from datetime import date
# Create your views here.
all_posts = [
    {
        "slug": 'Hike-in-the-mountains',
        'image': 'mountains.jpg',
        'author': 'vivek',
        'date': date(2024, 10, 9),
        'title': 'Mountain Hiking',
        'excerpt': 'Mountains are majestic natural formations that rise high above the surrounding landscape, offering breathtaking views and a sense of awe',
        "content": "Mountains are majestic natural formations that rise high above the surrounding landscape, offering breathtaking views and a sense of awe. These towering peaks, formed over millions of years, are home to diverse ecosystems and unique wildlife. Mountains challenge adventurers with their rugged terrain, while providing tranquility and inspiration to those who seek their solitude. Whether blanketed in snow or covered in lush forests, mountains are symbols of endurance, resilience, and the beauty of the natural world."
    },
    {
        "slug": 'Jungle-diaries',
        'image': 'woods.jpg',
        'author': 'vivek',
        'date': date(2023, 1, 6),
        'title': 'Jungle-diaries',
        'excerpt': 'Jungle Diaries is an immersive exploration of the wild, offering a captivating glimpse into the untamed world of dense forests and their inhabitants. ',
        "content": " Jungle Diaries is an immersive exploration of the wild, offering a captivating glimpse into the untamed world of dense forests and their inhabitants. Through vivid storytelling and stunning visuals, it delves into the daily lives of creatures, the delicate balance of ecosystems, and the raw beauty of nature. Whether focusing on the majesty of predators, the intricacies of plant life, or the hidden dramas of the jungle"
    },
    {
        "slug": 'Photography-skills',
        'image': 'download.jpeg',
        'author': 'vivek',
        'date': date(2024, 2, 7),
        'title': 'Photography',
        'excerpt': ' Photography is the art of capturing moments in time, freezing them in a frame to tell a story, evoke emotions, or document reality.',
        "content": " Photography is the art of capturing moments in time, freezing them in a frame to tell a story, evoke emotions, or document reality. Whether through the lens of a smartphone or a professional camera, photography allows us to see the world from different perspectives. It can highlight the beauty of everyday life, document historical events, or express creative visions. As both a hobby and a profession, photography is a powerful tool for communication, preserving memories, and inspiring others through visual storytelling"
    },
    {
        "slug": 'Movie-time',
        'image': 'movie.jpeg',
        'author': 'vivek',
        'date': date(2024, 1, 19),
        'title': 'Cinema',
        'excerpt': 'Cinema is a powerful art form that combines visual storytelling, sound, and motion to create immersive experiences.',
        "content": " Cinema is a powerful art form that combines visual storytelling, sound, and motion to create immersive experiences. It has the ability to transport audiences to different worlds, evoke deep emotions, and reflect society's complexities. From the golden age of Hollywood to contemporary independent films, cinema continues to evolve, shaping culture and influencing generations. Whether through blockbuster spectacles or intimate indie projects, cinema remains a central medium for entertainment, education, and artistic expression."
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {'posts': latest_posts})


def posts(request):
    return render(request, "blog/all-posts.html", {'all_posts': all_posts})


def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {
        'post': identified_post
    })
