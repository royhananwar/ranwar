<template>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-light fixed-top">
        <div class="container">
            <a class="navbar-brand" href="javascript:;" @click="goHome()">Home</a>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:;" @click="goBlog()">Blog</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:;" @click="goAbout()">Animals</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="javascript:;" @click="goAnimals()">About</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    app: 'BlogNavbar',
    methods: {
        goHome () {
            this.$router.push('/')
        },
        goBlog() {
            this.$router.push('/blog')
        },
        goAbout() {
            this.$router.push('/about')
        },
        goAnimals() {
            this.$router.push('/animals')
        }
    }
}
</script>

