const fs = require("fs");
const superagent = require("superagent");

const readFilePro = (file) => {
  return new Promise((resolve, reject) => {
    fs.readFile(file, (err, data) => {
      if (err) reject("I could not find that file");
      resolve(data);
    });
  });
};

const writeFilePro = (file, data) => {
  return new Promise((resolve, reject) => {
    fs.writeFile(file, data, (err) => {
      if (err) reject("Could not find the file");
      resolve("success");
    });
  });
};

const getDogPic = async () => {
  try {
    const data = await readFilePro(`${__dirname}/dog.txt`);
    console.log(`breed ${data}`);

    const res1pro = superagent.get(
      `https://dog.ceo/api/breed/${data}/images/random`
    );
    const res2pro = superagent.get(
      `https://dog.ceo/api/breed/${data}/images/random`
    );
    const res3pro = superagent.get(
      `https://dog.ceo/api/breed/${data}/images/random`
    );

    const all = await Promise.all([res1pro, res2pro, res3pro]);
    const imgs = all.map((el) => el.body.message);
    console.log(imgs);

    await writeFilePro("dog-img.txt", imgs.join("\n"));
    console.log("Work done 😶");
  } catch (e) {
    console.log(e);
    throw e;
  }
  return "2: Ready Beyatch";
};

(async () => {
  try{
    console.log('1: Will get DOuge pic')
    const x = await getDogPic()
    console.log(x)
    console.log('3: done getting douge pic')
  }catch(err){
    console.log("ERRORWRW")
  }
})()

// console.log("1: Will get DOuge pic");
// const x = getDogPic();
// console.log(x);
// console.log("3: done getting douge pic");

// console.log('1: Will get DOuge pic')
// getDogPic()
// .then(x => {
//   console.log(x)
//   console.log('3: done getting douge pic')
// })
// .catch(err => {
//   console.log("ERRORWRW")
// })

// readFilePro(`${__dirname}/dog.txt`)
//   .then((data) => {
//     console.log(`breed ${data}`);
//     return superagent.get(`https://dog.ceo/api/breed/${data}/images/random`);
//   })
//   .then((res) => {
//     console.log(res.body.message);
//     return writeFilePro("dog-img.txt", res.body.message);
//   })
//   .then(() => {
//     console.log("random lol");
//   })
//   .catch((err) => console.log(err.message));
