    import os
    import shutil
    import zipfile

    # masirhaye asli
    drive_d = "D:/"
    drive_e = "E:/"
    final_folder_name = "Final_Folder"

    # ejade poshe haye makhsos dar drive D
    text_folder = os.path.join(drive_d, "Text_Files")
    image_folder = os.path.join(drive_d, "Images")
    video_folder = os.path.join(drive_d, "Videos")

    # function makhsos enteghal file ha be poshe haye marbot
    def organize_files():
        if not os.path.exists(text_folder):
            os.makedirs(text_folder)
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
        if not os.path.exists(video_folder):
            os.makedirs(video_folder)
        
        # jabejaee file be poshe haye marbot
        for file_name in os.listdir(drive_d):
            file_path = os.path.join(drive_d, file_name)
            
            # barresi type of file
            if os.path.isfile(file_path):
                if file_name.endswith(('.txt', '.doc', '.docx', '.pdf')):
                    shutil.move(file_path, text_folder)
                elif file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                    shutil.move(file_path, image_folder)
                elif file_name.endswith(('.mp4', '.avi', '.mov', '.mkv')):
                    shutil.move(file_path, video_folder)

    # enteghal posheha be drive E
    def move_folders_to_drive_e():
        for folder in [text_folder, image_folder, video_folder]:
            shutil.move(folder, drive_e)

    # jame avari va enteghal anha be poshe nahayee va ejade file zip
    def create_final_zip():
        final_folder_path = os.path.join(drive_e, final_folder_name)
        if not os.path.exists(final_folder_path):
            os.makedirs(final_folder_path)

        # enteghal poshe ha be poshe nahayee
        for folder_name in ["Text_Files", "Images", "Videos"]:
            shutil.move(os.path.join(drive_e, folder_name), final_folder_path)
        
        # ejade file zip az poshe nahayee
        zip_file_path = os.path.join(drive_e, f"{final_folder_name}.zip")
        with zipfile.ZipFile(zip_file_path, 'w') as zipf:
            for root, dirs, files in os.walk(final_folder_path):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), final_folder_path))

    # ejraye marahel
    organize_files()
    move_folders_to_drive_e()
    create_final_zip()

    print(" Tamome ! ")
