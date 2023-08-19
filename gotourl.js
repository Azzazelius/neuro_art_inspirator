console.log('\nACTION!\n');
const button = document.getElementById("clickGO")


function getRandom(num) {
  console.log('\nRANDOM GO\n');
  return Math.floor(Math.random() * (num + 1));
}

function goto(){
  console.log('\nGOTO\n');

  const fileURL = 'styles_list.txt';
  const xhr = new XMLHttpRequest();
  xhr.open('GET', fileURL, true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      const content = xhr.responseText;
      const lines = content.split('\n');
      const index = getRandom(lines.length);
      const line = lines[index];
      console.log(index);
  
      const url = `https://www.midlibrary.io/styles/${line}`;
      console.log(url);
    
      window.open(url, '_blank');
    }
  };
  xhr.send();
}

button.addEventListener('click', function() {goto()});