# Face-photo-sketch-synthesis-and-Recognition
In this project we aim to present a simple Face Photo-Sketch Synthesis and Recognition
system. FSS(Face Sketch Synthesis) provides a way to compare and match the faces present
in two different modalities (i.e face-photos and face-sketches). We can reduce the difference
between photo and sketch significantly and decrease the texture irregularity between them
by converting the photo to a sketch or vice-versa. This results in effective matching between
the two thus simplifying the process of recognition.
This system is modeled using three major components:
i) For a given input face-photo, obtaining an output face-sketch
ii) For a given input face-sketch, obtaining an output face-photo
iii) Recognition of the face-photo or the face-sketch in the database for a given query
face-sketch or face-photo respectively

<b>Find the project's research paper here:</b> https://doi.org/10.1007/978-3-031-12413-6_7
## Sample Results
![face_sketch_photo_synthesis_outputs](https://github.com/user-attachments/assets/ae622fc7-8563-47b1-aed1-75f5f5983886)

## Face sketch synthesis 
![Screenshot 2024-02-03 200328](https://github.com/mitravinda462/Face-photo-sketch-synthesis-and-Recognition/assets/53876415/94f7e4a4-0ceb-4de8-9c9e-e7936b042052)

### Files required 
Photo-Sketch.py 
input.jpg 
### Commands: 
	python3 Photo-Sketch.py 
(give path to input images in Photo-Sketch.py file in ‘path=’/images’’) 

## Face photo synthesis
![Screenshot 2024-02-03 200456](https://github.com/mitravinda462/Face-photo-sketch-synthesis-and-Recognition/assets/53876415/d9d2a036-d64c-42b1-a944-7ab34b94e70f)

### Files required 
haarcascade_frontalface_default.xml <br>
training_output_cropped.npy <br>
training_input_cropped.npy <br>
detect_face.py <br>
fetch_data.py <br>
Photo-Sketch.py <br>
train_model.py <br>
Prediction.py <br>
CelebA Dataset 
### Commands : 
	python3 detect_face.py
	python3 fetch_data.py 
	python3 Photo-Sketch.py 
	python3 train_model.py 
	python3 Prediction.py path_to_sketch.jpg 

## Facial recognition
![Screenshot 2024-02-03 200533](https://github.com/mitravinda462/Face-photo-sketch-synthesis-and-Recognition/assets/53876415/fc14842b-d95e-44dd-a9c2-6412511f190c)

### Requirements : 
ORL dataset 
### Commands : 
	python3 Face_recognition.py

