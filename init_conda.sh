read -p "Create bot_venv? (y/n): " venvAnswer

if [[ "$venvAnswer" == "y" || "$venvAnswer" == "Y" ]]; then
  conda create -n bot_venv python=3.12
fi

conda init zsh