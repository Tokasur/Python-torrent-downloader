import libtorrent as lt
import time
import argparse

def download_torrent(torrent_input, save_path):
    # Configuration de la session
    ses = lt.session()
    settings = {
        'listen_interfaces': '0.0.0.0:6881,[::]:6881',
        'enable_dht': True
    }
    ses.apply_settings(settings)

    # Création des paramètres de torrent
    params = lt.add_torrent_params()
    params.save_path = save_path
    params.storage_mode = lt.storage_mode_t.storage_mode_sparse

    # Gestion des différents types d'entrée
    if torrent_input.startswith('magnet:'):
        params = lt.parse_magnet_uri(torrent_input)
        params.save_path = save_path
    else:
        info = lt.torrent_info(torrent_input)
        params.ti = info

    # Configuration des flags
    params.flags = (
        lt.torrent_flags.duplicate_is_error 
        | lt.torrent_flags.auto_managed 
        | lt.torrent_flags.duplicate_is_error
    )

    handle = ses.add_torrent(params)
    
    print("Démarrage du téléchargement...")
    
    while not handle.status().is_seeding:
        status = handle.status()
        
        print(f"\rProgression: {status.progress * 100:.2f}% - "
              f"Vitesse: {status.download_rate / 1000:.1f} kB/s - "
              f"Upload: {status.upload_rate / 1000:.1f} kB/s - "
              f"Pairs: {status.num_peers}", end=' ', flush=True)
        
        time.sleep(1)
    
    print("\nTéléchargement terminé !")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Téléchargeur Torrent')
    parser.add_argument('source', type=str, help='Chemin du fichier .torrent ou lien magnet')
    parser.add_argument('-o', '--output', type=str, default='.', help='Répertoire de sauvegarde')
    args = parser.parse_args()

    download_torrent(args.source, args.output)
