<template>
    <v-layout justify-center align-center>
        <v-flex xs5>
            <v-select
                v-model="client.selected"
                :items="clients"
                :item-text="'firstname'"
                :item-value="'id'"
                label="Selecione um Cliente"
                @change="changeClient($event)"
                required
                >
            </v-select>
            <v-btn color="success" :to="{name: 'client-register'}">Cadsatrar Cliente</v-btn>
            <v-btn color="success" @click="handleCamera">
                <span v-if="!camera.on">Ligar Camera</span>
                <span v-else>Fechar Camera</span>
            </v-btn>
            <v-btn v-show="camera.on" color="success" @click="captureCient">
                <span>Tirar Foto</span>
            </v-btn>
            <v-btn v-show="camera.on && camera.takePhoto" color="success" @click="validateClient">
                <span>Validar Cliente</span>
            </v-btn>
        </v-flex>
        <v-flex xs12>
            <video v-show="camera.on" ref="camera" :width="450" :height="337.5" autoplay></video>
        </v-flex>
        <v-flex xs12>
            <canvas v-show="camera.takePhoto" id="takePhoto" ref="canvas" :width="450" :height="337.5"></canvas>
        </v-flex>
    </v-layout>
</template>
<script>
import AppApi from '~apijs'

export default {
  data () {
    return {
        camera: {
            on: false,
            takePhoto: false,
        },
        client: {
            selected: 0,
            photo: '',
        },
        clients: []
    }
  },
  methods: {
    handleCamera() {
      if (this.camera.on) {
          this.camera.on = false;
          this.camera.takePhoto = false;
          this.shutDownCamera();
      } else {
          this.camera.on = true;
          this.initCamera();
      }
    },
    initCamera() {
      const args = (window.args = {
        audio: false,
        video: true
      });
      
      navigator.mediaDevices
        .getUserMedia(args)
        .then(stream => {
            this.$refs.camera.srcObject = stream;
        })
        .catch(error => {
            console.log(error);
            alert("Opa, parece que seu navegador não suporta essa opreção!");
        });
    },
    shutDownCamera() {
      let camTracks = this.$refs.camera.srcObject.getTracks();

      camTracks.forEach(track => {
        track.stop();
      });
    },
    captureCient() {
        this.camera.takePhoto = true;
        const ctx = this.$refs.canvas.getContext('2d');
        ctx.drawImage(this.$refs.camera, 0, 0, 450, 337.5);
    },
    validateClient() {
        const photoTaked = document.getElementById("takePhoto").toDataURL("image/jpeg");
        var self = this;
        var requestJS = AppApi;
        this.urlToFile(photoTaked, 'client.jpeg', 'image/jpeg').then(function (file) {
            self.client.photo = file;
            console.log(self.client);
            requestJS.validate_client(self.client).then(response => {
                const accuracy = response.data;
                console.log(accuracy);
            });
        });
        
    },
    changeClient(value) {
        this.client.selected = value;
        console.log(value);
    },
    getClients() {
        AppApi.list_clients().then(response => {
            const clients = response.data;
            this.clients = clients.clients;
        });
    },
    urlToFile(url, filename, extension) {
        return (fetch(url)
            .then(function (response) {
                return response.arrayBuffer();
            })
            .then(function (buffer) {
                return new File([buffer], filename, {
                    type: extension
                }) 
            }))
    }
  },
  mounted() {
      this.getClients();
  },
}
</script>