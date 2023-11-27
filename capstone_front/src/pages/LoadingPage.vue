<template>
    <q-page>
        <div class="flex flex-center">
            <div class="img-container">
                <img class="img" style="width: 400px;" src="~assets/load.gif">
            </div>
        </div>
    </q-page>
</template>

<style>
.img-container {
    width: 100%; 
        height: 100vh; 
        display: -webkit-box; 
        display: -moz-box;
        display: -ms-flexbox; 
        display: flex;

        -webkit-box-align: center; 
        -moz-box-align: center;
        -ms-flex-align: center;
        align-items: center; /* 수직 정렬 */
 
        -webkit-box-pack: center;
        -moz-box-pack: center; 
        -ms-flex-pack: center; 
        justify-content: center;
}
</style>