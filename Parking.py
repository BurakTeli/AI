import cv2
import pickle
# işaretlidğimde kayıtlı olması için
try:
    with open("Otopark_algılama","rb") as f:
        liste=pickle.load(f)
except:
    liste = []

def mouse(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        liste.append((x,y))
    if events == cv2.EVENT_LBUTTONDOWN:
        for l, pos in enumerate(liste):
            x1,y1=pos
            if x1<x<x1+26 and y1<y<y1+15:
                liste.pop(l)
    with open("Otopark_algılama","wb") as f:
        pickle.dump(liste, f)


while True:
    img = cv2.imread("Otopark_foto.png")
    print(liste)

    for i in liste:
        cv2.rectangle(img,i,(i[0]+26,i[1]+15),(255,0,0),2) # değişebilir fotoya göre

    cv2.imshow("pen",img)
    cv2.setMouseCallback("pen",mouse)
    if cv2.waitKey(1) &0xFF == ord("q"):
        break



cv2.destroyAllWindows()


