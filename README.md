# price_analyzer

```bash
git clone git@github.com:akchau/price_analyzer.git
cd price_analyzer
python -m venv venv
source venv/bin/activate
pip install -r req.txt
nano .env
```
туда добавить путь к папке где будут лежать прайсы
вот пример как у меня
PRICE_DIR=/home/dev/price_analyzer/data

```bash
python main.py
```

Консольная утилита для поиска в прайс-листах.