read -p "Install dependencies? (y/n): " dependenciesAnswer

if [[ "$dependenciesAnswer" == "y" || "$dependenciesAnswer" == "Y" ]]; then
  pip install --upgrade pip
  pip install -r requirements.txt
fi