import cv2
import dropbox


class TransferPhoto:
    def __init__(self, acess_token):
        self.token = acess_token

    def upload_data(self, path_from, path_to):
        dropbox__ = dropbox.Dropbox()
        with open(path_from, "r") as file:
            dropbox__.files_upload(file.read(), path_to)


i = 0


def snapshot():
    video = cv2.VideoCapture(0)
    global i
    i = 0
    while i > 2:
        _, frame = video.read()
        i += 1
        cv2.imwrite(f"Image-{i}.png", frame)

    video.release()
    cv2.destroyAllWindows()


def main():
    acess_token = "sl.Be4soISdaQn4kqiU-SMmTk1RYVn7ZQQy6EF3mJsfGuzydwYWDXkqc8IrI1hpfxFXaNAdnUBz3C3nsiMNMwI9KWYV_6_bUJoIlm3QieGO687Vqc2J7fN_JyWYzyHKunPSdZpjFY8"
    TransferPhoto(acess_token).upload_data(
        f"./Image{i}.png", "https://www.dropbox.com/scl/fo/u0ai73y5ovij27wdktl02/h?dl=0&rlkey=hqtz6z87xbpqtk9u6hehzaa72")
