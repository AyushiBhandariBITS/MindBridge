from fastapi import APIRouter
from datetime import datetime

wellness_prompts = [
  "What are three things you are grateful for today?",
  "What small step can you take today to improve your mental health?",
  "How would you describe your mood today?",
  "Is there something you've been avoiding that you could face today?",
  "What is something you can do to practice self-care today?",
  "What is one thing you love about yourself?",
  "What personal strength can you celebrate today?",
  "What brings you peace and calm?",
  "What do you need to let go of today to feel lighter?",
  "What are your top three priorities today?",
  "What was the highlight of your day so far?",
  "Is there a habit you'd like to start today? What's one action you can take?",
  "What does your ideal day look like? How can you work toward it?",
  "What is one way you can be kind to yourself today?",
  "How do you feel physically today? Are there any areas of tension or discomfort?",
  "What is one thing you can do to nourish your body today?",
  "Who are you grateful for in your life right now?",
  "What's a recent achievement, big or small, that you're proud of?",
  "What are you looking forward to in the coming days or weeks?",
  "When was the last time you laughed? What brought you joy?",
  "What's something you can do today that will make you feel accomplished?",
  "How are you feeling emotionally today? What emotions are you experiencing?",
  "What's something you can do to reduce stress in your life today?",
  "What's one goal you have for your emotional well-being?",
  "When was the last time you helped someone else? How did it make you feel?",
  "What's a hobby or activity you've been wanting to explore?",
  "What's your favorite way to unwind after a busy day?",
  "What's one way you can show gratitude for your body today?",
  "How can you incorporate more movement into your day today?",
  "What's one positive affirmation you can repeat today?",
  "What's something you've learned recently that you're proud of?",
  "How can you connect with nature today?",
  "What's a thought pattern you want to let go of today?",
  "How can you make time for joy today?",
  "What's one small act of kindness you can do for someone else today?",
  "What are you looking to achieve in the next week? How can you start today?",
  "What's one thing you'd like to forgive yourself for?",
  "What's one thing that always makes you smile?",
  "What's your favorite self-care activity and why?",
  "What would it look like if you lived with no fear or anxiety for today?",
  "How do you define success today?",
  "What's something you'd like to improve in your daily routine?",
  "What's one way you can slow down and enjoy the present moment today?",
  "What's your biggest source of stress at the moment? How can you address it?",
  "What's one way you can make time for creativity today?",
  "What's a healthy boundary you need to set with yourself or others?",
  "What are some ways you can prioritize your mental health this week?",
  "What's something you can do today to feel connected to others?",
  "What is one change you'd like to make in your lifestyle?",
  "What's a positive quality in others that you admire?",
  "What is something you've been meaning to say to someone?",
  "What does your ideal self-care routine look like?",
  "How do you practice mindfulness in your daily life?",
  "What's one thing you want to accomplish before the end of the month?",
  "What's one way you can be more present in your interactions with others?",
  "How do you feel about the direction your life is heading right now?"
]


def get_daily_prompt():
    # Select prompt based on the current day
    date = datetime.today().date()
    prompt_index = date.day % len(wellness_prompts)  # Debugging line to check the index
    return wellness_prompts[prompt_index]

router = APIRouter()

@router.get("/")
async def get_daily_prompt_endpoint():
    prompt = get_daily_prompt()  # Get prompt of the day
    return {"prompt": prompt}
