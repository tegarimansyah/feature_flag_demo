<template>
    <div class="container">
        <div class="flex flex-col bg-gray-700 md:flex-row w-screen">
            <Sidebar />

            <div class="main-content flex-1 bg-grey-lightest pb-24 md:pb-5 content-center bg-white">

                <div class="bg-blue-darker p-2 shadow text-xl">
                    <h3 class="pl-2">User Management</h3>
                </div>

                <div class="flex flex-wrap">
                    <!-- Add User -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <div class="bg-green-lightest border-b-4 border-green-dark rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-green-dark"><i class="fa fa-wallet fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">Add New User</h5>
                                    <h3 class="text-3xl">+ <span class="text-green"><i class="fas fa-caret-up"></i></span></h3>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- Edit User -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <div class="bg-green-lightest border-b-4 border-green-dark rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-green-dark"><i class="fa fa-wallet fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">Edit User</h5>
                                    <h3 class="text-3xl">Search... <span class="text-green"><i class="fas fa-caret-up"></i></span></h3>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- List User -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <div class="bg-green-lightest border-b-4 border-green-dark rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-green-dark"><i class="fa fa-wallet fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">List User</h5>
                                    <h3 class="text-3xl">Search... <span class="text-green"><i class="fas fa-caret-up"></i></span></h3>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Role Set up -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <div class="bg-green-lightest border-b-4 border-green-dark rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-green-dark"><i class="fa fa-wallet fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">Role Set Up</h5>
                                    <h3 class="text-3xl">+ <span class="text-green"><i class="fas fa-caret-up"></i></span></h3>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Permission Set up -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <div class="bg-green-lightest border-b-4 border-green-dark rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-green-dark"><i class="fa fa-wallet fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">Permission Set Up</h5>
                                    <h3 class="text-3xl">+ <span class="text-green"><i class="fas fa-caret-up"></i></span></h3>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>


</template>

<script>
import Sidebar from '~/components/Sidebar.vue'

export default {
  components: {
    Sidebar
  }
}
</script>