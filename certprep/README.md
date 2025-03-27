# Certification Practice Exam Implementation

## File Structure
```
exam-practice/
    ├── index.html
    ├── styles.css
    ├── app.js
    ├── questions.js
    ├── data/
        ├── aws-associate.json
        ├── gcp-associate.json
        └── python-cert.json
```

## How to Set Up
1. Create a folder named `exam-practice` (or any name you prefer) in your GitHub Pages repository
2. Add all the files according to the structure above
3. Make sure the questions JSON files are in the same directory as the HTML/JS files

## Adding More Certifications
1. Create a new JSON file (e.g., `azure-fundamentals.json`) with your questions
2. Add the certification to the `certifications` object in `questions.js`:
   ```javascript
   "azure-fundamentals": {
       id: "azure-fundamentals",
       name: "Microsoft Azure Fundamentals (AZ-900)",
       file: "azure-fundamentals.json"
   }
   ```

## JSON Structure for Questions
Each certification's JSON file should contain an array of question objects with this structure:

```json
[
    {
        "id": 1,
        "text": "Your question text here",
        "options": [
            { "id": "a", "text": "Option A" },
            { "id": "b", "text": "Option B" },
            { "id": "c", "text": "Option C" },
            { "id": "d", "text": "Option D" }
        ],
        "correctAnswers": ["b"],
        "explanation": "Explanation of the correct answer",
        "multipleSelect": false
    }
]
```

For multiple-select questions, set `multipleSelect` to `true` and include all correct answers in the `correctAnswers` array.

## Running Locally
For local testing, use a simple server like Python's http.server module:
```python
python -m http.server 8000
```

Then access your app through: http://localhost:8000/

## Troubleshooting
If questions don't load:
1. Check browser console for errors
2. Verify that JSON files are correctly formatted
3. Make sure file paths are correct
4. Check that JSON files are accessible to JavaScript (no CORS issues)