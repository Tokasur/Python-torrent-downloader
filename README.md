# Python-torrent-downloader
A python script for downloading torrents

# Python Torrent Downloader CLI  
# Téléchargeur Torrent Python en Ligne de Commande

🇬🇧 English | [🇫🇷 Français]

---

## 🤖 Project Overview / Aperçu du Projet
**Personal project developed with AI assistance**  
**Projet personnel développé avec assistance IA**  

---

## 🚀 Features / Fonctionnalités
- 📥 Supports .torrent files and magnet links
- 📊 Real-time statistics (progress/speed/peers)
- 🐧 Linux optimized (Tested on Debian 12)
- 💡 Minimal dependencies

*Prend en charge :*
- 📥 Fichiers .torrent et liens magnet
- 📊 Statistiques temps réel
- 🐧 Optimisé pour Linux (Debian 12)
- 💡 Dépendances minimales

---
### Prerequisites / Prérequis
python3 and python3-libtorrent

For debian use sudo apt install python3 python3-libtorrent

git git-core to use git clone

## ⚙️ Installation

git clone https://github.com/Tokasur/Python-torrent-downloader.git
cd Python-torrent-downloader

🛠️ Usage / Utilisation

# Basic usage
python3 torrent_downloader.py [TORRENT_FILE_OR_MAGNET] -o ./download folder of your choice

# Example with .torrent
python3 torrent_downloader.py example.torrent -o ~/Downloads

# Example with magnet
python3 torrent_downloader.py "magnet:?xt=..." -o ./movies

"" requis for magnet or torrent file with space

Options :

--help       Show help message
--output -o  Set download directory (default: current)

⚠️ Important Notes / Notes Importantes

🔒 Legal Warning: Only download authorized content
🔒 Légal : Téléchargez uniquement du contenu autorisé
