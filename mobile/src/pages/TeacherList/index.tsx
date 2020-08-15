import React, { useState} from 'react'
import { View, ScrollView, Text, TextInput } from 'react-native'
import { Feather} from '@expo/vector-icons'
import AsyncStorage from '@react-native-community/async-storage'


import PageHeader from '../../components/PageHeader'

import styles from './styles'
import TeacherItem, { Teacher } from '../../components/TeacherItem'
import { BorderlessButton, RectButton } from 'react-native-gesture-handler'
import api from '../../services/api'
import { useFocusEffect } from '@react-navigation/native'

function TeacherList() {
    const [teachers, setTeachers] = useState([])
    const [favorites, setFavorites] = useState<number[]>([])
    const [isFiltersVisible, setIsFiltersVisible] = useState(false)

    const [subject, setSubject] = useState('')
    const [week_day, setWeekDay] = useState('')
    const [time, setTime] = useState('')

    function loadFavorites(){
        AsyncStorage.getItem('favorites').then(response => {
            if(response){
                const favoritedTeachers =  JSON.parse(response)
                const favoritedTeachersIds = favoritedTeachers.map((teacher: Teacher) => {
                    return teacher.id
                })

               setFavorites(favoritedTeachersIds)
            }
        })
    }

    function handleToggleFilterVisible(){
        setIsFiltersVisible(!isFiltersVisible)
    }


    async function handleFilterSubmit(){
        loadFavorites()
        const response = await api.get('classes', {
            params:{
                subject,
                week_day,
                time,
            }
        })
        
        console.log(response.data)

        setTeachers(response.data)
    }

    return (
        <View style={styles.container}>
            <ScrollView>
            <PageHeader 
                title="Proffys disponíveis" 
                headerRight={(
                    <BorderlessButton onPress={handleToggleFilterVisible} >
                        <Feather name="filter" size={20} color='#FFF'/>
                    </BorderlessButton>
                )} 
                
            >
                {isFiltersVisible && (
                    <View style={styles.searchForm}>
                        <Text style={styles.label}>Matéria</Text>
                        <TextInput
                            style={styles.input}
                            value={subject}
                            onChangeText={text => setSubject(text)}
                            placeholder="Qual a matéria?"
                            placeholderTextColor='#c1bccc'
                        />

                        <View style={styles.inputGroup}>
                            <View style={styles.inputBlock}>
                                <Text style={styles.label}>Dia da semana</Text>
                                <TextInput
                                    style={styles.input}
                                    value={week_day}
                                    onChangeText={text => setWeekDay(text)}
                                    placeholder="Qual o dia?"
                                    placeholderTextColor='#c1bccc'
                                />
                            </View>

                            <View style={styles.inputBlock}>
                                <Text style={styles.label}>Horário</Text>
                                <TextInput
                                    style={styles.input}
                                    value={time}
                                    onChangeText={text => setTime(text)}
                                    placeholder="Qual o dia?"
                                    placeholderTextColor='#c1bccc'
                                />
                            </View >
                        </View>

                        <RectButton onPress={handleFilterSubmit}  style={styles.submitButton}>
                            <Text style={styles.submitButtonText}>Filtar</Text>
                        </RectButton>
                    </View>
                )}
            </PageHeader>

            <View style={styles.teacherItemRend}>
                {teachers.map((teacher: Teacher) => {
                    return (
                        <TeacherItem 
                            key={teacher.id}  
                            teacher={teacher} 
                            favorited={favorites.includes(teacher.id)}
                         />)
            })}
            </View>

            </ScrollView>
        </View>
    )

}

export default TeacherList