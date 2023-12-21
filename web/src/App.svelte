<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'

  import { onMount } from 'svelte';

  let data: string;

  onMount(async () => {
    const response = await fetch('/api/getRandom');
    data = await response.text();
  });
</script>

<main>
  <h1>Flask + Nginx + Vite + Svelte</h1>

  <div class="card">
    <Counter />
  </div>

  <p>Random number: {data}</p>
</main>
