#!/bin/sh -x
curl -X 'POST' \
  'http://localhost:8068/question' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H "authorization: Bearer $ACCESS_TOKEN" \
  -d '{
  "type": 1,
  "question_text": "This is an example Multiple Choice Question",
  "choices": [
    {
      "text": "Wrong Answer",
      "choice_id": 0
    },
    {
      "text": "Correct Answer",
      "choice_id": 1
    }
  ],
  "answer": {
    "text": null,
    "correct_choice_ids": [
      1
    ]
  }
}' | jq
