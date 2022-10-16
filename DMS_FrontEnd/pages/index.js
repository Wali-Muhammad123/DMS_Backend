import Head from 'next/head';
import Image from 'next/image';
import HeaderNav from '../components/HeaderNav';
import HeroImage from '../assets/images/heroImage.png';

export default function CamoLogin() {
  return (
    <div>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <HeaderNav />
      <main className="mt-5">
        <div className="container">
          <div className="row">
            <div className="col">
              <p className="hero_text">
                Torrential monsoon rains triggered the most severe flooding in Pakistan’s recent history, washing away villages and leaving almost 10
                million children in need of immediate, lifesaving support. in need of assistance and at increased risk of waterborne diseases,
                drowning and malnutrition.
              </p>
            </div>
            <div class="col">
              <Image src={HeroImage} alt="Hero Image" />
            </div>
          </div>
        </div>
      </main>
    </div>
  );
}
