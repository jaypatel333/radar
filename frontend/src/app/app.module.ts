import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ClarityModule } from '@clr/angular';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { DataService } from './services/data.service';
import { HttpClientModule } from '@angular/common/http';
import { OneComponent } from './components/one/one.component';

import { Routes, RouterModule } from '@angular/router';
import { TwoComponent } from './components/two/two.component';
import { ThreeComponent } from './components/three/three.component';
import { FourComponent } from './components/four/four.component';
import { FiveComponent } from './components/five/five.component';
import { SixComponent } from './components/six/six.component';
import { SevenComponent } from './components/seven/seven.component';
import { EightComponent } from './components/eight/eight.component';
import { NineComponent } from './components/nine/nine.component';
import { TenComponent } from './components/ten/ten.component';

const routes: Routes = [
  { path: '1', component: OneComponent , pathMatch: 'full' },
  { path: '2', component: TwoComponent , pathMatch: 'full' },
  { path: '3', component: ThreeComponent , pathMatch: 'full' },
  { path: '4', component: FourComponent , pathMatch: 'full' },
  { path: '5', component: FiveComponent , pathMatch: 'full' },
  { path: '6', component: SixComponent , pathMatch: 'full' },
  { path: '7', component: SevenComponent , pathMatch: 'full' },
  { path: '8', component: EightComponent , pathMatch: 'full' },
  { path: '9', component: NineComponent , pathMatch: 'full' },
  { path: '10', component: TenComponent , pathMatch: 'full' }

];

@NgModule({
  declarations: [
    AppComponent,
    OneComponent,
    TwoComponent,
    ThreeComponent,
    FourComponent,
    FiveComponent,
    SixComponent,
    SevenComponent,
    EightComponent,
    NineComponent,
    TenComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ClarityModule,
    BrowserAnimationsModule,
    HttpClientModule,
    RouterModule.forRoot(routes)
  ],
  providers: [DataService],
  bootstrap: [AppComponent]
})
export class AppModule { }
