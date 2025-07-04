name: Deploy Dev

on:
  push:
    branches: [ dev ]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Deploy to EC2 (dev)
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ${{ secrets.EC2_USER }}
          key: ${{ secrets.EC2_KEY }}
          script: |
            cd snapshot-dev
            git pull origin dev
            docker-compose down
            docker-compose up --build -d
