<template>
  <v-form v-model="valid">
    <v-container>
      <v-layout>
        <v-flex
          xs12
          md4
        >
          <v-text-field
            v-model="user.firstname"
            :rules="user.nameRules"
            :counter="10"
            label="First name"
            required
          ></v-text-field>
        </v-flex>

        <v-flex
          xs12
          md4
        >
          <v-text-field
            v-model="user.lastname"
            :rules="user.nameRules"
            :counter="10"
            label="Last name"
            required
          ></v-text-field>
        </v-flex>

        <v-flex
          xs12
          md4
        >
          <v-text-field
            v-model="user.email"
            :rules="user.emailRules"
            label="E-mail"
            required
          ></v-text-field>
        </v-flex>
        <v-flex
          xs12
          md12>
          <input type="file" @change="setDocument" name="photo" accept="image/*">
        </v-flex>
      </v-layout>
      <v-btn color="success" @click="register">Cadastrar Cliente</v-btn>
    <v-btn color="success" :to="{name: 'client-validate'}">Validar Cliente</v-btn>
    </v-container>
  </v-form>
</template>
<script>
  import AppApi from '~apijs'
  export default {
    data: () => ({
      valid: false,
      user: {
            firstname: '',
            lastname: '',
            email: '',
            document: '',
            nameRules: [
                v => !!v || 'Name is required',
                v => v.length <= 10 || 'Name must be less than 10 characters'
            ],
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+/.test(v) || 'E-mail must be valid'
            ]
      }
    }),
    methods: {
        register() {
            console.log(this.user);
            AppApi.register_client(this.user).then(response => {
                const client = response.data;
                if (typeof client.id !== "undefined") {
                    alert("Client cadastrado com sucesso");
                    this.$router.push({
                        'path': '/'
                    });
                } else {
                    alert("Falha ao cadastrar cliente");
                }
            });
        },
        setDocument() {
            this.user.document = document.querySelector('input[type=file]')
                .files[0];
        }
    },
  }
</script>