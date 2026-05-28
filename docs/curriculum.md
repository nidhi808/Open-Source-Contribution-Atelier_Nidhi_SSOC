# Curriculum and Lesson Management Guide

This guide explains how the learning curriculum is structured, how to add new lessons and exercises, and how the Django backend serializes them for the React frontend.

---

## 🏗️ Architecture Overview

The learning track is fully driven by the database, making it modular and easy to expand. It consists of two primary models inside the `apps.content` app:

1. **Lesson**: Holds the educational content, difficulty tier, tips, learning objectives, and ordering metadata.
2. **Exercise**: Holds the interactive task associated with a lesson, including the command prompt, expected command, explanation, and points.

---

## 🗄️ Database Models & Schema

### 1. Lesson Model (`apps/content/models.py`)
*   `title` (CharField): The display title of the lesson.
*   `slug` (SlugField, Unique): Unique URL identifier.
*   `difficulty` (CharField): Tier (`beginner`, `intermediate`, `advanced`).
*   `content` (TextField): Main educational text (supports Markdown).
*   `learning_objectives` (JSONField/ArrayField): Key takeaways.
*   `tips` (JSONField/ArrayField): Pro-tips shown in the sidebar.
*   `order` (IntegerField): Placement order in the curriculum.
*   `estimated_minutes` (IntegerField): Estimated reading/exercise completion time.

### 2. Exercise Model (`apps/content/models.py`)
*   `lesson` (ForeignKey -> Lesson): The parent lesson.
*   `title` (CharField): Name of the exercise.
*   `prompt` (TextField): The instruction displayed in the web terminal.
*   `expected_command` (CharField): The exact command the user must enter in the sandbox to pass.
*   `explanation` (TextField): The educational summary shown after correct execution.
*   `points` (IntegerField): Score awarded upon success.

---

## 🚀 How to Add or Modify Lessons

All default lessons are managed via a database seeding script. To add a new lesson:

### Step 1: Update the Seeding Script
Open `backend/apps/content/management/commands/seed_lessons.py` and append your new lesson dictionary to the `LESSONS` list:

```python
{
    "slug": "git-revert",
    "difficulty": "intermediate",
    "title": "Reverting Commits",
    "summary": "Safely undo changes without altering commit history.",
    "content": "Unlike git reset, git revert creates a new commit that undoes the changes of a previous commit. This is the safest way to undo on public branches.",
    "learning_objectives": [
        "Explain the difference between revert and reset",
        "Create a reverting commit"
    ],
    "tips": [
        "Always prefer git revert for public, shared branches."
    ],
    "order": 15,
    "estimated_minutes": 10,
    "exercises": [
        {
            "title": "Revert last commit",
            "prompt": "Create a revert commit for HEAD.",
            "expected_command": "git revert HEAD --no-edit",
            "explanation": "git revert creates a new commit that applies opposite changes.",
            "points": 10
        }
    ]
}
```

### Step 2: Run the Management Command
Apply your changes to your local database by running:
```bash
cd backend
python manage.py seed_lessons
```
> [!NOTE]
> The `seed_lessons` command is fully idempotent. Running it will update existing lessons in place and create any new ones without duplicating data.

---

## 🔌 API Integration & Serializers

The React frontend fetches the curriculum using REST endpoints. The serialization of the models is managed in `backend/apps/content/serializers.py`:

### 1. Exercise Serializer
The `ExerciseSerializer` handles the translation of the `Exercise` model. 
*   **Safety Rule:** The `expected_command` is excluded or handled securely so that users cannot inspect the browser's network requests to read the correct answer!

### 2. Lesson Serializers
*   `LessonListSerializer`: Serializes a high-level summary (title, difficulty, order, points) for the dashboard dashboard-cards list.
*   `LessonDetailSerializer`: Serializes the full content, learning objectives, tips, and embeds the nested `ExerciseSerializer` list to allow complete interactive rendering on the Lesson page.

### 3. Exposing New Fields
If you add a new field to either model (e.g. `icon` or `category`):
1. Add the field to the database model in `apps/content/models.py` and run migrations.
2. Update the `fields` list inside `apps/content/serializers.py`:
   ```python
   class LessonDetailSerializer(serializers.ModelSerializer):
       exercises = ExerciseSerializer(many=True, read_only=True)
       
       class Meta:
           model = Lesson
           fields = ['id', 'title', 'slug', 'difficulty', 'content', 'learning_objectives', 'tips', 'order', 'estimated_minutes', 'exercises', 'your_new_field']
   ```
3. Update the frontend TypeScript interfaces in `frontend/src/` to parse and render the new attribute.
