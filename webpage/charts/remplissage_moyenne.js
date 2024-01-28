function toggleZoom(element) {
    element.classList.toggle("zoomOut");
}
function initialiserSelecteurImages(idSelecteur, images, path, idimage, defaultImage) {
    const imageSelector = document.getElementById(idSelecteur);
    const displayedImage = document.getElementById(idimage);

    // Add the placeholder option
    const placeholderOption = document.createElement('option');
    placeholderOption.value = '';
    if (idSelecteur=="imageSelectorbikes"){
        placeholderOption.textContent = 'Choisissez une image pour les parkings vélos';
    }
    else{
        placeholderOption.textContent = 'Choisissez une image pour les parkings voiture';
    }
    imageSelector.appendChild(placeholderOption);

    // Add other options
    images.forEach(image => {
        const option = document.createElement('option');
        option.value = image;
        option.textContent = image;
        imageSelector.appendChild(option);
    });

    imageSelector.addEventListener('change', function() {
        if (this.value) {
            displayedImage.src = path + this.value + '.png';
            displayedImage.alt = this.value;
        } else {
            // Set the src attribute to the default image path
            displayedImage.src = defaultImage;
            displayedImage.alt = 'Image sélectionnée apparaîtra ici';
        }
    });

    displayedImage.onerror = function() {
        console.error("L'image ne peut pas être chargée : " + this.src);
    };
}
function handleChartSelect() {
    var select = document.getElementById("chartSelect");
    var selectedValue = select.options[select.selectedIndex].value;
    if (selectedValue !== "") {
        // Perform the redirection or other actions here
        location.href = selectedValue;
    }
}


document.addEventListener('DOMContentLoaded', function() {
    
    const images = ['Antigone', 'Comedie', 'Corum', 'Europa', 'Foch', 'Gambetta', 'Gare', 'Triangle', 'Pitot', 'Circe', 'Garcia Lorca', 'Mosson', 'Sabines', 'Sablassou', 'Saint Jean Le Sec', 'Euromedecine', 'Occitanie', 'Vicarello', 'Gaumont EST', 'Gaumont OUEST', 'Charles de Gaulle', 'Polygone', 'Arc de Triomphe']; 
    const path = '/webpage/charts/charts/moyenne_remplissage/cars/avg_cars-'
    const idimage = 'displayedImagecars'
   
    

    defaultImageCars = '/webpage/charts/charts/moyenne_remplissage/cars/avg_cars-total.png';
    
    initialiserSelecteurImages('imageSelectorcars', images, path, idimage,defaultImageCars);
});
document.addEventListener('DOMContentLoaded', function() {
    
    const images = ['Rue Jules Ferry - Gare Saint-Roch', 'Comédie', 'Hôtel de Ville', 'Corum', 'Place Albert 1er - St Charles', 'Foch', 'Halles Castellane', 'Observatoire', 'Rondelet', 'Plan Cabanes', 'Boutonnet', 'Emile Combes', 'Beaux-Arts', 'Les Aubes', 'Antigone centre', 'Médiathèque Emile Zola', 'Nombre d Or', 'Louis Blanc', 'Gambetta', 'Port Marianne', 'Les Arceaux', 'Cité Mion', 'Nouveau Saint-Roch', 'Renouvier', 'Odysseum', 'Saint-Denis', 'Richter', 'Charles Flahault', 'Voltaire', 'Prés d Arènes', 'Garcia Lorca', 'Vert Bois', 'Malbosc', 'Occitanie', 'FacdesSciences', 'Fac de Lettres', 'Aiguelongue', 'Jeu de Mail des Abbés', 'Euromédecine', 'Marie Caizergues', 'Sabines', 'Celleneuve', 'Jardin de la Lironde', 'Père Soulas', 'Place Viala', 'Hôtel du Département', 'Tonnelles', 'Parvis Jules Ferry - Gare Saint-Roch', 'Pont de Lattes - Gare Saint-Roch', 'Deux Ponts - Gare Saint-Roch', 'Providence - Ovalie', 'Pérols Etang de l Or', 'Albert 1er - Cathédrale', 'Saint-Guilhem - Courreau', 'Sud De France', 'Comedie Baudin', 'Jean de Beins']; 
    const path ='/webpage/charts/charts/moyenne_remplissage/bikes/avg_bikes-'
    const idimage = "displayedImagebike"

    
    defaultImageBikes = '/webpage/charts/charts/moyenne_remplissage/bikes/avg_bikes-total.png'


    initialiserSelecteurImages('imageSelectorbikes', images ,path, idimage,defaultImageBikes);
});

