pwd

rm -rf .compile
mkdir -p .compile

cp -R /src/dbx .compile/dbx

cp /src/setup.py .compile/setup.py
cp dbx.spec .compile/dbx.spec

cd /src

pip install --upgrade pip && pip install -r requirements.txt

bumpversion patch 

cd /.dist

pyinstaller --distpath=platforms/debian .compile/dbx.spec
