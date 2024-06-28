from fastpunct import FastPunct
import pysrt
import googletrans as gt
import pysubs2 as ps

def punctuate(srtPath):
  print("Punctuating.....")
  fastpunct = FastPunct()
  subs = pysrt.open(srtPath)

  for sub in subs:
    s=''
    s=str(s+str(fastpunct.punct([sub.text])))

    with open(srtPath,'r') as file:
      content = file.read()
    content = content.replace(sub.text,s[2:-2])
    with open(srtPath, 'w') as file:
      file.write(content)

def translate(srtPath):
  print("Translating.....")
  
  subs = ps.load(srtPath)
  translator = gt.Translator()

  for line in subs:
      text = line.text
      #print(text)
      try:
          line.text = translator.translate(text=text, dest='kn').text
      except:
          print("error")

  subs.save(srtPath)