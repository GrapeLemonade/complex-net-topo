import io
import os
import zipfile

for dirpath, dirnames, filenames in os.walk(os.curdir):
    for dir in dirnames:
        if dir.startswith('.'):
            continue
        dd = os.path.join(os.curdir, dir)
        for dps, dns, fns in os.walk(dd):
            for fn in fns:
                file_path = os.path.join(dd, fn)
                if fn.endswith('.cfg'):
                    pass
                elif fn.endswith('.zip'):
                    extract_to_dir = dd
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(extract_to_dir)
                        print(f'Extracted {file_path}')
                elif fn.endswith('efz'):
                    start_signature = b'\x50\x4B\x03\x04'
                    end_signature = b'\x50\x4B\x05\x06'
                    with open(file_path, 'rb') as f:
                        flash = f.read(2 ** 20)
                        st = flash.find(start_signature)
                        ed = flash.find(end_signature, st) + 22
                        # print(flash[st:ed])
                        zip_bytes = io.BytesIO(flash[st:ed])
                        # zipfile.
                        # with open('qwq.zip', 'wb') as ff:
                        #     ff.write(flash[st:ed])
                        try:
                            with zipfile.ZipFile(zip_bytes, 'r') as zip_ref:
                                with open(os.path.join(dd, 'vrpcfg.cfg'), 'wb') as ff:
                                    ff.write(zip_ref.read('vrpcfg.cfg'))
                                print(f'Extracted {file_path}')
                        except zipfile.BadZipFile as e:
                            print(f'{e}: {file_path}')
                else:
                    print(f'Unrecongnized file {file_path}')
        # if filename.endswith('.zip'):
        #     zip_file_path = os.path.join(dirpath, filename)
        #     extract_to_dir = os.path.join(dirpath, filename[:-4])  # Extract to a directory with the zip file's name
            
        #     # Create the extraction directory if it does not exist
        #     if not os.path.exists(extract_to_dir):
        #         os.makedirs(extract_to_dir)
            
        #     # Extract the zip file
        #     with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        #         zip_ref.extractall(extract_to_dir)
        #         print(f'Extracted {zip_file_path} to {extract_to_dir}')
