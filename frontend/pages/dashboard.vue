<template>
    <div class="container">
        <div class="flex flex-col bg-gray-700 md:flex-row w-screen">
            <Sidebar />

            <div class="main-content flex-1 bg-grey-lightest pb-24 md:pb-5 content-center bg-white">

                <div class="bg-blue-darker p-2 shadow text-xl">
                    <h3 class="pl-2">Dashboard</h3>
                </div>

                <div class="flex flex-wrap">
                    <!-- Total Revenue -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <!--Metric Card-->
                        <div class="bg-green-lightest border-b-4 border-green-dark rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-green-dark"><i class="fa fa-wallet fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">Total Revenue</h5>
                                    <h3 class="text-3xl">$3249 <span class="text-green"><i class="fas fa-caret-up"></i></span></h3>
                                </div>
                            </div>
                        </div>
                        <!--/Metric Card-->
                    </div>
                    <!-- New User -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <!--Metric Card-->
                        <div class="bg-yellow-lightest border-b-4 border-yellow-dark rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-yellow-dark"><i class="fas fa-user-plus fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">New Users</h5>
                                    <h3 class="text-3xl">2 <span class="text-yellow-dark"><i class="fas fa-caret-up"></i></span></h3>
                                </div>
                            </div>
                        </div>
                        <!--/Metric Card-->
                    </div>
                    <!-- Total User -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <!--Metric Card-->
                        <div class="bg-orange-lightest border-b-4 border-orange rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-orange-dark"><i class="fas fa-users fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">Total Users</h5>
                                    <h3 class="text-3xl">249 <span class="text-orange"><i class="fas fa-exchange-alt"></i></span></h3>
                                </div>
                            </div>
                        </div>
                        <!--/Metric Card-->
                    </div>
                    <!-- Server Uptime -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <!--Metric Card-->
                        <div class="bg-blue-lightest border-b-4 border-blue rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-blue-dark"><i class="fas fa-server fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">Server Uptime</h5>
                                    <h3 class="text-3xl">152 days</h3>
                                </div>
                            </div>
                        </div>
                        <!--/Metric Card-->
                    </div>
                    <!-- Issue -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <!--Metric Card-->
                        <div class="bg-red-lightest border-b-4 border-red rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-red-dark"><i class="fas fa-inbox fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">Issues</h5>
                                    <h3 class="text-3xl">3 <span class="text-red"><i class="fas fa-caret-up"></i></span></h3>
                                </div>
                            </div>
                        </div>
                        <!--/Metric Card-->
                    </div>
                    <!-- To Do List -->
                    <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <!--Metric Card-->
                        <div class="bg-indigo-lightest border-b-4 border-indigo rounded-lg shadow-lg p-5">
                            <div class="flex flex-row items-center">
                                <div class="flex-shrink pr-4">
                                    <div class="rounded-full p-5 bg-indigo-dark"><i class="fas fa-tasks fa-2x fa-inverse"></i></div>
                                </div>
                                <div class="flex-1 text-right md:text-center">
                                    <h5 class="uppercase text-grey-dark">To Do List</h5>
                                    <h3 class="text-3xl">7 tasks</h3>
                                </div>
                            </div>
                        </div>
                        <!--/Metric Card-->
                    </div>
                </div>


                <div class="flex flex-row flex-wrap flex-grow mt-2">

                    <!-- Table -->
                    <div class="w-full md:w-full xl:w-full p-3">
                        <!--Table Card-->
                        <div class="bg-white border-transparent rounded-lg shadow-lg">
                            <div class="bg-grey-light border-b-2 border-grey rounded-tl-lg rounded-tr-lg p-2">
                                <h5 class="uppercase text-grey-dark">Table</h5>
                            </div>
                            <div class="p-5">
                                <table class="w-full p-5 text-grey-darker">
                                    <thead>
                                        <tr>
                                            <th class="text-left text-blue-darkest">Name</th>
                                            <th class="text-left text-blue-darkest">Side</th>
                                            <th class="text-left text-blue-darkest">Role</th>
                                        </tr>
                                    </thead>

                                    <tbody>
                                        <tr>
                                            <td>Obi Wan Kenobi</td>
                                            <td>Light</td>
                                            <td>Jedi</td>
                                        </tr>
                                        <tr>
                                            <td>Greedo</td>
                                            <td>South</td>
                                            <td>Scumbag</td>
                                        </tr>
                                        <tr>
                                            <td>Darth Vader</td>
                                            <td>Dark</td>
                                            <td>Sith</td>
                                        </tr>
                                    </tbody>
                                </table>

                                <p class="py-2"><a href="#">See More issues...</a></p>

                            </div>
                        </div>
                        <!--/table Card-->
                    </div>

                    <!-- Template Card-->
                    <!-- <div class="w-full md:w-1/2 xl:w-1/3 p-3">
                        <div class="bg-white border-transparent rounded-lg shadow-lg">
                            <div class="bg-grey-light border-b-2 border-grey rounded-tl-lg rounded-tr-lg p-2">
                                <h5 class="uppercase text-grey-dark">Template</h5>
                            </div>
                            <div class="p-5">

                            </div>
                        </div>
                    </div> -->

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

